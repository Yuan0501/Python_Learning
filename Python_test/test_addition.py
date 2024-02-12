import addition
import sys

# pytest is not in this working directory path, so insert the file first
sys.path.insert(1, r'/Users/yuanyuanzhu/Library/Python/3.9/bin')
import pytest

# write test function, using assert filename.funcionname()
def test_add():
    assert addition.add(4, 5) == 9


def test_sub():
    pass


# To run the test file:
# Open terminal and type "python3 -m pytest test_addition.py"
# Tip: terminal path should be on the working directory, you can use "cd filename" to change the terminal working directory 

