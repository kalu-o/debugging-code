```markdown
# Debugging Code


## Table of Contents
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup-and-installation)
- [Running the Code](#running-the-code)
- [Running Tests](#running-tests)

## Project Structure

The repository is structured as follows:

```
.
├── data                # Sample data files used in the course
├── docs                # Documentation files (course outline)
├── README.md           # This file
├── requirements.txt    # List of dependencies
├── src                 # Source code for the exercise in Chapter 4
└── test                # Test cases and scripts
```

## Prerequisites

The following settings are used:

- Python 3.10
- `virtualenv` (optional)

## Project Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kalu-o/debugging-code.git
   cd debugging-code
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - On **macOS and Linux**:

     ```bash
     source venv/bin/activate
     ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Code (Exercise)

The Python script provided in the `src` directory contains some errors that prevent it from running successfully. Your tasks are:
- Creaate a test script in the `test` directory
- Run the test
- Debug and fix the script `src/process_sales_data.py`

## Running Tests

To execute the test cases, run from the root repository:

```bash
pytest test/
```


