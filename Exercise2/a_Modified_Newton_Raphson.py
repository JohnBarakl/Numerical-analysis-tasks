import math
from math import sin
from math import cos


def modified_newton_raphson(function, function_derivative, function_second_derivative, starting_point, digits_of_precision):
    iteration_counter = 0

    f = function
    f_d = function_derivative
    f_dd = function_second_derivative

    x = starting_point

    while True:
        if f(x) == 0:
            return x, iteration_counter
        else:
            iteration_counter += 1
            x_next = x - (f(x) / f_d(x)) - (1/2) * ( (f(x) ** 2 * f_dd(x)) / (f_d(x)**3) )

            if abs(x_next - x) < 0.5 * 10 ** (-1.0 * digits_of_precision):
                return x_next, iteration_counter
            else:
                x = x_next


def f(x):
    return 94 * (cos(x) ** 3) - 24 * cos(x) + 177 * (sin(x) ** 2) - 108 * (sin(x) ** 4) - 72 * (cos(x) ** 3) * (sin(x) ** 2) - 65


def f_derivative(x):
    return - 282 * (cos(x) ** 2) * sin(x) + 24 * sin(x) + 354 * sin(x) * cos(x) - 432 * (sin(x) ** 3) * cos(x) + 216 * (cos(x) ** 2) * (sin(x) ** 3) - 144 * (cos(x) ** 4) * sin(x)


def f_second_derivative(x):
    return 564 * cos(x) * (sin(x) ** 2) - 282 * (cos(x) ** 3) + 24 * cos(x) + 354 * (cos(x) ** 2) - 354 * (sin(x) ** 2) - 1296 * (cos(x) ** 2) * (sin(x) ** 2) + 432 * (sin(x) ** 4) - 432 * cos(x) * (sin(x) ** 4) \
           + 648 * (cos(x) ** 3) * (sin(x) ** 2) + 576 * (cos(x) ** 3) * (sin(x) ** 2) - 144 * (cos(x) ** 5)


if __name__ == '__main__':
    root, loops_counter = modified_newton_raphson(f, f_derivative, f_second_derivative, 0.8, 5)
    print("The root near 0.8: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

    root, loops_counter = modified_newton_raphson(f, f_derivative, f_second_derivative, 1.0, 5)
    print("The root near 1.05: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

    root, loops_counter = modified_newton_raphson(f, f_derivative, f_second_derivative, 2.3, 5)
    print("The root near 2.25: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))
