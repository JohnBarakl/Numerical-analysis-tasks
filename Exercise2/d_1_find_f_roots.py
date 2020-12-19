from Exercise2.a_Modified_Newton_Raphson import modified_newton_raphson
from Exercise2.b_Modified_Bisection import modified_bisection
from Exercise2.c_Modified_Secant import modified_secant

import math
from math import sin, cos


def f(x):
    return 94 * (cos(x) ** 3) - 24 * cos(x) + 177 * (sin(x) ** 2) - 108 * (sin(x) ** 4) - 72 * (cos(x) ** 3) * (sin(x) ** 2) - 65


def f_derivative(x):
    return - 282 * (cos(x) ** 2) * sin(x) + 24 * sin(x) + 354 * sin(x) * cos(x) - 432 * (sin(x) ** 3) * cos(x) + 216 * (cos(x) ** 2) * (sin(x) ** 3) - 144 * (cos(x) ** 4) * sin(x)


def f_second_derivative(x):
    return 564 * cos(x) * (sin(x) ** 2) - 282 * (cos(x) ** 3) + 24 * cos(x) + 354 * (cos(x) ** 2) - 354 * (sin(x) ** 2) - 1296 * (cos(x) ** 2) * (sin(x) ** 2) + 432 * (sin(x) ** 4) - 432 * cos(x) * (sin(x) ** 4) \
           + 648 * (cos(x) ** 3) * (sin(x) ** 2) + 576 * (cos(x) ** 3) * (sin(x) ** 2) - 144 * (cos(x) ** 5)


print("Modified Newton-Raphson roots:")
root, loops_counter = modified_newton_raphson(f, f_derivative, f_second_derivative, 0.8, 5)
print("\tThe root near 0.8: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_newton_raphson(f, f_derivative, f_second_derivative, 1.0, 5)
print("\tThe root near 1.0: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_newton_raphson(f, f_derivative, f_second_derivative, 2.3, 5)
print("\tThe root near 2.3: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))


print("\nModified Bisection roots:")
root, loops_counter = modified_bisection(f, 0.8, 1.0, 5)
print("\tThe root in [0.8, 1.0]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_bisection(f, 1.0, 1.2, 5)
print("\tThe root in [1.0, 1.2]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_bisection(f, 2.2, 2.4, 5)
print("\tThe root in [2.2, 2.4]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))


print("\nModified Secant roots:")
root, loops_counter = modified_secant(f, 0.8, 0.85, 0.9, 5)
print("\tThe root in [0.8, 0.9]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_secant(f, 1.0, 1.1, 1.2, 5)
print("\tThe root in [1.0, 1.2]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_secant(f, 2.0, 2.25, 2.5, 5)
print("\tThe root in [2.0, 2.5]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))
