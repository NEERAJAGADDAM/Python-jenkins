import unittest
from src.example import add_numbers, Subtract_numbers

class TestExample(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(100,200), 300)
        
    def test_subtract_numbers(self):
        self.assertEqual(add_numbers(300,200), 100)
        
if __name__ == "__main__":
    unittest.main()
        