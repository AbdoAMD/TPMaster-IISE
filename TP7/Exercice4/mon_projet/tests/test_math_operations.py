# tests/test_math_operations.py

import unittest
from src import addition, soustraction, multiplication, division

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(-1, -1), -2)

    def test_soustraction(self):
        self.assertEqual(soustraction(10, 5), 5)
        self.assertEqual(soustraction(-1, 1), -2)
        self.assertEqual(soustraction(-1, -1), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 7), 21)
        self.assertEqual(multiplication(-1, 1), -1)
        self.assertEqual(multiplication(-1, -1), 1)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(-1, 1), -1)
        self.assertEqual(division(-1, -1), 1)
        with self.assertRaises(ZeroDivisionError):
            division(1, 0)

if __name__ == "__main__":
    unittest.main()
