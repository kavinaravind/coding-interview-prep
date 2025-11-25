import sys
import os
from pathlib import Path

# 1. Template for the file content
TEMPLATE = """import pytest

class Solution:
    def solve(self, args):
        \"\"\"
        [Problem Description]

        Approach:
        [Algorithm Description]

        Time Complexity: O(...)
            - [Analysis]

        Space Complexity: O(...)
            - [Analysis]

        Difficulty: [Easy/Medium/Hard]
        \"\"\"
        pass

class TestSolution:
    @pytest.mark.parametrize("args, expected", [
        ("test_input", "expected_output"),
    ])
    def test_solve(self, args: str, expected: str) -> None:
        sol = Solution()
        # assert sol.solve(args) == expected
        pass
"""

def create_problem():
    # 2. Parse Arguments
    if len(sys.argv) < 3:
        print("Usage: python3 scripts/generate.py <number> <name>")
        print('Example: python3 scripts/generate.py 1 "Two Sum"')
        sys.exit(1)

    number = sys.argv[1]
    name = sys.argv[2]

    # 3. Format folder name: "1" -> "0001", "Two Sum" -> "two-sum"
    folder_num = number.zfill(4)
    folder_slug = name.lower().replace(" ", "-").replace("'", "")
    folder_name = f"{folder_num}-{folder_slug}"

    # 4. Define paths
    # Assuming this script is in /scripts, we go up one level to root, then into src/solutions
    base_dir = Path(__file__).parent.parent / "src" / "solutions"
    target_dir = base_dir / folder_name
    target_file = target_dir / "solution.py"

    # 5. Create Directory
    if target_dir.exists():
        print(f"Error: Directory {target_dir} already exists!")
        sys.exit(1)
    
    os.makedirs(target_dir)

    # 6. Write File
    with open(target_file, "w") as f:
        f.write(TEMPLATE)

    print(f"✅ Created: {target_dir}")
    print(f"📄 File: {target_file}")

if __name__ == "__main__":
    create_problem()