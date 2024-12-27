import unittest
from file import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-3, -5), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(10, -4), 6)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 7), 7)
        self.assertEqual(add_numbers(7, 0), 7)

    def test_add_floats(self):
        self.assertAlmostEqual(add_numbers(2.5, 3.1), 5.6)

# if __name__ == "__main__":
#     unittest.main()
