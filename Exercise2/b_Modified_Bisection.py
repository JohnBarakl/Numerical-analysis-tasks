import math
from math import sin
from math import cos
import random

def modified_bisection(function, range_beginning, range_ending, digits_of_precision):
    iteration_counter = 0

    f = function
    a = range_beginning
    b = range_ending
    fa = f(a)
    fb = f(b)

    m = random.uniform(a, b)
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


def f(x):
    return 94 * (cos(x) ** 3) - 24 * cos(x) + 177 * (sin(x) ** 2) - 108 * (sin(x) ** 4) - 72 * (cos(x) ** 3) * (sin(x) ** 2) - 65


if __name__ == "b_Modified_Bisection":
    root, loops_counter = modified_bisection(f, 0.8, 1.0, 5)
    print("The root in [0.8, 0.95]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

    root, loops_counter = modified_bisection(f, 1.0, 1.1, 5)
    print("The root in [1.0, 1.1]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

    root, loops_counter = modified_bisection(f, 2.2, 2.4, 5)
    print("The root in [2.2, 2.4]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

    print()

    print("First root:")
    temp_sum = 0
    for i in range(10):
        root, loops_counter = modified_bisection(f, 0.8, 1.0, 5)
        temp_sum += loops_counter
        print("\tRoot: {:f} calculated in {:d} repetitions".format(root, loops_counter))
    print("\tMean: {:f} repetitions".format(temp_sum/10))

    print("Second root:")
    temp_sum = 0
    for i in range(10):
        root, loops_counter = modified_bisection(f, 1.0, 1.1, 5)
        temp_sum += loops_counter
        print("\tRoot: {:f} calculated in {:d} repetitions".format(root, loops_counter))
    print("\tMean: {:f} repetitions".format(temp_sum/10))

    print("Third root:")
    temp_sum = 0
    for i in range(10):
        root, loops_counter = modified_bisection(f, 2.2, 2.4, 5)
        temp_sum += loops_counter
        print("\tRoot: {:f} calculated in {:d} repetitions".format(root, loops_counter))
    print("\tMean: {:f} repetitions".format(temp_sum/10))
