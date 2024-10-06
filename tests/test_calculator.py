import unittest
import qadro_calculate

class TestCalculator(unittest.TestCase):

    def test_add_positive(self):
        result = qadro_calculate.qadro(2)
        self.assertEqual(result, 4)


    def test_add_negative(self):
        result = qadro_calculate.qadro(-1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()