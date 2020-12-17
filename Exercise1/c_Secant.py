import math
from math import sin
from math import e


def f(x):
    return e ** (sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1


def secant(function, point_one, point_two, digits_of_precision):
    iteration_counter = 0

    f = function

    x1 = point_one
    x2 = point_two

    while True:
        if f(x2) == 0:
            return x2, iteration_counter
        else:
            iteration_counter += 1
            x_next = x2 - (f(x2) * (x2 - x1)) / (f(x2) - f(x1))

            if abs(x_next - x2) < 0.5 * 10 ** (-1.0 * digits_of_precision):
                return x_next, iteration_counter
            else:
                x1 = x2
                x2 = x_next


root, loops_counter = secant(f, -1.5, -1.0, 5)
print("The root in [-1.5, -1.0]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = secant(f, -0.5, 0.5, 5)
print("The root in [-0.5, 0.5]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = secant(f, 1.25, 1.75, 5)
print("The root in [1.25, 1.75]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))
