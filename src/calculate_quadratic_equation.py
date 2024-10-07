from math import sqrt


def calculate_quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError

    d = b * b - 4 * a * c

    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        return -b / (2 * a)

    return None
