import math
from math import sin
from math import cos

def modified_secant(function, point_one, point_two, point_three, digits_of_precision):
    iteration_counter = 0

    f = function

    x1 = point_one
    x2 = point_two
    x3 = point_three

    while True:
        if f(x3) == 0:
            return x3, iteration_counter
        else:
            iteration_counter += 1

            q = f(x1) / f(x2)
            r = f(x3) / f(x2)
            s = f(x3) / f(x1)

            x_next = x3 - ( r * (r - q) * (x3 - x2) + (1 - r) * s * (x3 - x1) ) / ( (q - 1) * (r - 1) * (s - 1) )

            if abs(x_next - x3) < 0.5 * 10 ** (-1.0 * digits_of_precision):
                return x_next, iteration_counter
            else:
                x1 = x2
                x2 = x3
                x3 = x_next


def f(x):
    return 94 * (cos(x) ** 3) - 24 * cos(x) + 177 * (sin(x) ** 2) - 108 * (sin(x) ** 4) - 72 * (cos(x) ** 3) * (sin(x) ** 2) - 65


if __name__ == "c_Modified_Secant":
    root, loops_counter = modified_secant(f, 0.8, 0.85, 0.9, 5)
    print("The root in [0.8, 0.9]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

    root, loops_counter = modified_secant(f, 1.0, 1.1, 1.2, 5)
    print("The root in [1.0, 1.2]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

    root, loops_counter = modified_secant(f, 2.0, 2.25, 2.5, 5)
    print("The root in [2.0, 2.5]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))
