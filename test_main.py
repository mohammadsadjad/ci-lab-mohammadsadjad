import unittest
from main import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
    def test_add_incorrect(self):
        self.assertEqual(add(2, 2), 4)  # Fixed test
if __name__ == '__main__':
    unittest.main()