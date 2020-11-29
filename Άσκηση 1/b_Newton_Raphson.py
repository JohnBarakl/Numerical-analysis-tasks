import math
from math import sin
from math import cos
from math import e


def f(x):
    return e ** (sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1  # Ορισμός της f(x)


def f_derivative(x):
    return 3 * (sin(x) ** 2) * cos(x) * (
            e ** (sin(x) ** 3)) + 6 * x ** 5 - 8 * x ** 3 - 3 * x ** 2  # Η παράγωγος της f(x)


def newton_raphson(function, function_derivative, starting_point, digits_of_precision):
    f = function
    f_d = function_derivative

    x = starting_point
    fx = f(x)

    x_next = 0  # Ορισμός του x_next
    while True:
        if fx == 0:
            return x
        else:
            x_next = x - f(x) / f_d(x)

        if abs(x_next - x) < 0.5 * 10 ** (-1.0 * digits_of_precision):
            return x_next
        else:
            x = x_next


print("Η ρίζα στο διάστημα [-2, -0.5]: ", newton_raphson(f, f_derivative, -1.25, 5))
print("Η ρίζα στο διάστημα [-0.5,0.5]: ", newton_raphson(f, f_derivative, 0, 5))
print("Η ρίζα στο διάστημα [0.5, 2]: ", newton_raphson(f, f_derivative, 1.5, 5))
