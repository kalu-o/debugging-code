
# Project: Debugging Code


## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup-and-installation)
- [Running the Code](#running-the-code)
- [Running Tests](#running-tests)


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


