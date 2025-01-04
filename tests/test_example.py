import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the functions to test
from example import add_numbers, Subtract_numbers  # Ensure this matches the function names in example.py


def test_add_numbers():
    assert add_numbers(10, 20) == 30
    assert add_numbers(-1, 1) == 0


def test_subtract_numbers():
    assert Subtract_numbers(5, 3) == 2  # Corrected the function name
    assert Subtract_numbers(3, 5) == -2  # Corrected the function name
