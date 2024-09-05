
# Project Title: Debugging Code


## Table of Contents
- [Introduction](#introduction)
- [Instructions](#instructions)
- [Packages and Functions](#packages-and-functions)
- [Dataset](#dataset)

## Introduction

Python is one of the most popular programming languages in data science. Writing code in Python is an essential skill for developers, but even the most experienced programmers encounter bugs that can be difficult to identify and resolve.

In this project, you will grasp the concept of debugging, be able to read error messages and identify the different types of errors. Furthermore, you will be exposed to simple debugging methods as well as advanced python debugging tools. By the end of this project, You will have improved your debugging skills. Prospective students should be intermediate Python programmers.

## Instructions

1. **Setup project:**  Install the required packages needed for the project.
2. **Load the dataset:** Load the provided dataset.
3. **Identify types of errors:** Identify `syntax`, `logical` and `runtime` errors.
4. **Handle exceptions:** Read, trace and understand error messages. Identify the function throwing exceptions and handle them.
5. **Use Python debugging tools:** First, use simple methods and later use debugging tools in Jupyter notebooks.
6. **Use tests for debugging:** Setup a unit test environment and write tests using pytest.

## Packages and Functions
### Packages
- pandas==2.2.2
- pytest-cov==5.0.0

### Functions
-  `load_data() `: loads the provided dataset.
- `calculate_sales_stats()`: calculates stats such as total sales, average sales and number of entries from the given dataset.
- `test_load_data()`: unit test for the `load_data()` function
- `test_calculate_sales_stats()`: unit test for the `calculate_sales_stats()` function

## Dataset

The dataset for this project is the ‘Sample Sales Data’ at  https://www.kaggle.com/datasets/kyanyoga/sample-sales-data
