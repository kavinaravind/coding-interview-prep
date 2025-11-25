import os
import re
from pathlib import Path
from typing import TypedDict


class Problem(TypedDict):
    number: str
    title: str
    slug: str
    difficulty: str
    path: str


ROOT_DIR = Path(__file__).parent.parent
SOLUTIONS_DIR = ROOT_DIR / "src" / "solutions"
README_PATH = ROOT_DIR / "README.md"

BASE_URL = "https://leetcode.com/problems/"


def get_difficulty(file_path: Path) -> str:
    """
    Reads the solution file and looks for a line like:
    Difficulty: Easy
    """
    if not file_path.exists():
        return "Unknown"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        match = re.search(r"\s*Difficulty:\s*(\w+)", content, re.IGNORECASE)
        if match:
            return match.group(1).title()
    return "Unknown"


def generate_table() -> None:
    if not SOLUTIONS_DIR.exists():
        print("No solutions directory found.")
        return

    # 1. Collect all problems
    problems: list[Problem] = []
    for item in os.listdir(SOLUTIONS_DIR):
        folder_path = SOLUTIONS_DIR / item
        if folder_path.is_dir() and not item.startswith("__") and not item.startswith(
            "."
        ):
            # Parse folder name: "0001-two-sum"
            parts = item.split("-", 1)
            if len(parts) != 2:
                continue

            number = parts[0]
            slug = parts[1]
            title = slug.replace("-", " ").title()

            # Find solution file
            sol_file = folder_path / "solution.py"
            difficulty = get_difficulty(sol_file)

            problems.append(
                {
                    "number": number,
                    "title": title,
                    "slug": slug,
                    "difficulty": difficulty,
                    "path": f"src/solutions/{item}/solution.py",
                }
            )

    # 2. Sort by number
    problems.sort(key=lambda p: int(p["number"]))

    # 3. Build Markdown Table
    table_lines = [
        "| Problem | Difficulty | Solution |",
        "| :--- | :--- | :--- |",
    ]

    for p in problems:
        leetcode_url = f"{BASE_URL}{p['slug']}/"
        problem_link = f"[{p['number']} {p['title']}]({leetcode_url})"
        row = f"| {problem_link} | {p['difficulty']} | [Python]({p['path']}) |"
        table_lines.append(row)

    new_table = "\n".join(table_lines)

    # 4. Inject into README
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Regex to replace content between markers
    pattern = r"(<!-- SOLUTIONS_START -->)(.*?)(<!-- SOLUTIONS_END -->)"
    replacement = f"\\1\n{new_table}\n\\3"

    new_readme, count = re.subn(
        pattern, replacement, readme_content, flags=re.DOTALL
    )

    if count == 0:
        print("Error: Could not find <!-- SOLUTIONS_START --> and <!-- SOLUTIONS_END --> in README.md")
    else:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("README.md updated successfully.")


if __name__ == "__main__":
    generate_table()