import unittest
from qadro_calculate import qadro

class TestCalculator(unittest.TestCase):

    def test_add_positive(self):
        result = qadro(1)
        self.assertEqual(result, 1)

    def test_add_negative(self):
        result = qadro(-1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()