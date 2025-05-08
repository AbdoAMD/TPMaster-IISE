# test_conversion.py

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Exercice1')))

import unittest
import conversion # type: ignore

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        with self.assertRaises(ValueError):
            conversion.dollars_to_dirhams(-10)
            
        result = conversion.dollars_to_dirhams(10)
        self.assertEqual(result, 98.0)
    
    def test_meters_to_kilometers(self):
        with self.assertRaises(ValueError):
            conversion.meters_to_kilometers(-1000)
            
        result = conversion.meters_to_kilometers(1500)
        self.assertEqual(result, 1.5)

if __name__ == "__main__":
    unittest.main()
