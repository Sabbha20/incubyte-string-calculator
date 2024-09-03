import unittest
from string_calculator import add


class TestStringCalculator(unittest.TestCase):
    def test_add_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_num_string(self):
        self.assertEqual(add("1"), 1)