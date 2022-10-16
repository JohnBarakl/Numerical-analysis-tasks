import random
import math
from math import sin, cos


def modified_bisection(function, range_beginning, range_ending, digits_of_precision):
    iteration_counter = 0

    f = function
    a = range_beginning
    b = range_ending
    fa = f(a)
    fb = f(b)

    r = random.uniform(a, b)
    fr = f(r)

    while True:
        if fr == 0:
            return r, iteration_counter
        elif fa * fr < 0:
            fb = fr
            b = r
        else:
            fa = fr
            a = r

        iteration_counter += 1

        old_r = r
        r = random.uniform(a, b)
        fr = f(r)

        if abs(old_r - r) < 0.5 * (10 ** (-1 * digits_of_precision)):
            return r, iteration_counter


def f(x):
    return 94 * (cos(x) ** 3) - 24 * cos(x) + 177 * (sin(x) ** 2) - 108 * (sin(x) ** 4) - 72 * (cos(x) ** 3) * (sin(x) ** 2) - 65


print("First root:")
for i in range(10):
    root, loops_counter = modified_bisection(f, 0.8, 1.0, 5)
    print("\tRoot: {:f} calculated in {:d} repetitions".format(root, loops_counter))

print("Second root:")
for i in range(10):
    root, loops_counter = modified_bisection(f, 1.0, 1.2, 5)
    print("\tRoot: {:f} calculated in {:d} repetitions".format(root, loops_counter))

print("Third root:")
for i in range(10):
    root, loops_counter = modified_bisection(f, 2.2, 2.4, 5)
    print("\tRoot: {:f} calculated in {:d} repetitions".format(root, loops_counter))
