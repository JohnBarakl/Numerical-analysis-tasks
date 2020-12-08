import math
from math import sin
from math import e


def f(x):
    return e ** (sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1  # The function definition


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


root, loops_counter = bisection(f, -2, -0.5, 5)
print("The root in the domain [-2, -0.5]: {:5f} was calculated in {:d} repetitions".format(round(root, 5), loops_counter))

root, loops_counter = bisection(f, 0.5, 2, 5)
print("The root in the domain [0.5, 2]: {:5f} was calculated in {:d} repetitions".format(round(root, 5), loops_counter))

