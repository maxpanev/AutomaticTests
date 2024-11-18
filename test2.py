import unittest
from lesson_AT01 import remainder

class TestDivide(unittest.TestCase):
    def test_remainder_success(self):
        self.assertEqual(remainder(8, 3), 2)

        self.assertEqual(remainder(10, 2), 0)
        self.assertNotEqual(remainder(10, 5), 1)


    def test_remainde_by_zero(self):
        self.assertRaises(ValueError, remainder, 2, 0)
        # self.assertRaises(TypeError, divide, 2, 0)

if __name__ == '__main__':
    unittest.main()