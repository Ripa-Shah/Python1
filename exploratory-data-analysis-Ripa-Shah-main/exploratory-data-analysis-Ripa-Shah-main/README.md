# HW-02: Exploratory Data Analysis

## Objectives

The learning objectives of this assignment are to:
1. Develop proficiency in Python for data visualization and exploratory data analysis.
2. Implement and test functions for data cleaning, outlier detection, and visualization.

## Setup Your Environment

Before starting, set up a Python environment. You will need to install the following tools and libraries:

- [Python (version 3.8 or higher)](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [pylint](https://pylint.pycqa.org/)

### Installing Dependencies

Install the required dependencies with:
```bash
pip install -r requirements.txt
```

## Check out the starter code

When you accepted the assignment, GitHub created a clone of the assignment
template for you at:

```
https://github.com/INFO-511-S25/exploratory-data-analysis-<your-username>
```

It also set up a separate `feedback` branch and a
[feedback pull request](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/leave-feedback-with-pull-requests)
that will allow the instructional team to give you feedback on your work.

**Note that Codespaces are enabled**:
To use a code space, click the green Code button, select the Codespaces tab, then Create codespace on main. 

**Alternatively, you can use your local machine**:
To get the assignment code on your local machine, clone the repository:
```bash
git clone https://github.com/INFO-511-S25/exploratory-data-analysis-<your-username>.git
```
You are now ready to begin working on the assignment.
You should do all your work in the default branch, `main`.

## File Descriptions

### `ds.py`
This is the main file where you will write your implementations. The file contains the following functions to complete:

1. `load_csv(file_path)`: Load a CSV file into a pandas DataFrame.
2. `data_summary(df)`: Generate a summary of the dataset, including shape, missing values, and data types.
3. `clean_missing_data(df)`: Handle missing data by filling numeric columns with their mean and non-numeric columns with their mode.
4. `detect_outliers(df, column)`: Identify outliers in a numeric column using the IQR method.
5. `visualize_column(df, column, title)`: Create a histogram to visualize the distribution of a numeric column.

### `test_ds.py`
This file contains automated tests for the functions in `ds.py`. Do not modify this file. It will verify the correctness of your implementation.

### `requirements.txt`
Lists the required Python packages for this assignment.

## Instructions

1. Open `ds.py` and implement the functions according to the docstrings provided.
2. Do **not** modify any other files.
3. Test your implementation by running the test suite.

## Running Tests

To verify your implementation, run the tests using `unittest`:
```bash
python -m unittest test_ds.py
```

- Initially, the tests will fail because no implementation exists.
- Once your code is correct, all tests will pass.

Example output when all tests pass:
```plaintext
============================= test session starts ==============================
...
collected 5 items

test_ds.py .....                                                  [100%]

============================== 5 passed in 0.05s ===============================
```

### Additional Checks

Ensure your code adheres to Python's coding standards by running `pylint`:
```bash
pylint ds.py
```

A perfect score looks like:
```plaintext
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## Submission Instructions

1. Commit your changes to `ds.py`:
   ```bash
   git add ds.py
   git commit -m "Implemented functions for HW-02"
   git push
   ```

2. Do **not** modify or merge the `test_ds.py` file or other files.

3. Ensure your tests pass on GitHub by checking the CI/CD results.

## Grading

### Points Allocation
- **80 points** for passing all automated correctness (`unittest`) tests.
- **10 points** for passing all automated quality (`pylint`) checks.
- **10 points** for overall code quality, including:
  - Using appropriate data structures.
  - Avoiding code duplication.
  - Giving variables meaningful names.
  - Documenting complex logic.

### Deductions
- Lose **5 points** for:
  - Modifying files other than `ds.py`.
  - Merging the "Feedback" pull request on GitHub.
  - Deleting or editing docstrings in `ds.py`.

Good luck, and happy coding!
