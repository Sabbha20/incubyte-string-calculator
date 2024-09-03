import unittest
from string_calculator import add


class TestStringCalculator(unittest.TestCase):
    def test_add_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_num_string(self):
        self.assertEqual(add("1"), 1)

    def test_comma_separated_num_string(self):
        self.assertEqual(add("2,3"), 5)
        self.assertEqual(add("3, 4"), 7)
        self.assertEqual(add("3, 4, 5, 6"), 18)

    def test_newline_num_string(self):
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("2,3\n4"), 9)
        
    def test_new_delimiter_input(self):
        self.assertEqual(add("//;\n1;2"), 3)
        self.assertEqual(add("//;\n2;3;4;1"), 10)