import math
from math import sin
from math import e


def f(x):
    return e ** (sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1


def bisection(function, range_beginning, range_ending, digits_of_precision):
    iteration_counter = 0

    f = function
    a = range_beginning
    b = range_ending
    fa = f(a)
    fb = f(b)

    m = (a + b) / 2
    fm = f(m)

    while True:
        if fm == 0:
            return m, iteration_counter
        elif fa * fm < 0:
            fb = fm
            b = m
        else:
            fa = fm
            a = m

        iteration_counter += 1

        old_m = m
        m = (a + b) / 2
        fm = f(m)

        if abs(old_m - m) < 0.5 * (10 ** (-1 * digits_of_precision)):
            return m, iteration_counter


root, loops_counter = bisection(f, -1.5, -1, 5)
print("The root in [-1.5, -1.0]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = bisection(f, 1.25, 1.75, 5)
print("The root in [1.25, 1.75]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = bisection(f, -0.5, 0.5, 5)
print("The root in [-0.5, 0.5]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))
