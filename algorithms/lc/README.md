# LeetCode Solutions

This directory contains solutions to LeetCode problems, organized by problem number.

## Project Structure

- `pyproject.toml`: Defines project metadata and dependencies.
- `src/solutions/`: Contains the solution and tests for each problem in its own directory.
- `src/datastructures/`: Contains utility code shared across different solutions.

## Setup

### Prerequisites

- Python 3.8+

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

## Running Tests

All tests are written using the `pytest` framework.

To run all tests, make sure you are in the `algorithms/lc` directory and run:

```bash
pytest
```
