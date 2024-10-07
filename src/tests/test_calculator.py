import unittest
from src.calculate_quadratic_equation import calculate_quadratic_equation

class TestQuadraticEquation(unittest.TestCase):

    def test_two_real_roots(self):
        # Проверяем случай, когда дискриминант > 0 (две разные корни)
        result = calculate_quadratic_equation(1, -3, 2)
        self.assertEqual(result, (2.0, 1.0))  # x1 = 2, x2 = 1

    def test_one_real_root(self):
        # Проверяем случай, когда дискриминант = 0 (один корень)
        result = calculate_quadratic_equation(1, -2, 1)
        self.assertEqual(result, 1.0)  # x = 1

    def test_no_real_roots(self):
        # Проверяем случай, когда дискриминант < 0 (нет реальных корней)
        result = calculate_quadratic_equation(1, 0, 1)
        self.assertIsNone(result)  # Нет решений

    def test_linear_equation(self):
        # Проверяем случай, когда a = 0 (линейное уравнение — ошибка)
        with self.assertRaises(ValueError):
            calculate_quadratic_equation(0, 2, 1)

if __name__ == '__main__':
    unittest.main()
