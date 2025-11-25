# LeetCode Solutions

This directory contains solutions to LeetCode problems, organized by problem number.

## Project Structure

- `src/solutions/`: Contains the solution and tests for each problem in its own directory.
- `src/datastructures/`: Contains utility code shared across different solutions.

## Setup

### Prerequisites

- Python 3.12+

### Environment Setup and Dependencies

1.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
2.  **Install dependencies:**
    The project uses `pyproject.toml` to manage dependencies. To install the necessary packages for running tests, use the following command.
    ```bash
    pip install -e ".[test]"
    ```

## Usage

**Generating a New Problem**

Using a helper script to generate the folder structure and boilerplate code (including test stubs).

```bash
python3 scripts/generate.py <number> "<Name>" # python3 scripts/generate.py 217 "Contains Duplicate"
```

**Updating the README**

Using a helper script to automatically update the Solutions Log in this README.

```bash
python3 scripts/update_readme.py
```

## Running Tests

All tests are written using the `pytest` framework.

To run all tests, make sure you are in the `algorithms/lc` directory and run:

```bash
pytest
```

## Solutions Log

<!-- SOLUTIONS_START -->

| Problem                                                                              | Difficulty | Solution                                                        |
| :----------------------------------------------------------------------------------- | :--------- | :-------------------------------------------------------------- |
| [0001 Two Sum](https://leetcode.com/problems/two-sum/)                               | Easy       | [Python](src/solutions/0001-two-sum/solution.py)                |
| [0021 Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy       | [Python](src/solutions/0021-merge-two-sorted-lists/solution.py) |
| [0125 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)             | Easy       | [Python](src/solutions/0125-valid-palindrome/solution.py)       |

<!-- SOLUTIONS_END -->
