import math
from math import sin, cos
import random


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


def classic_bisection(function, range_beginning, range_ending, digits_of_precision):
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

def classic_newton_raphson(function, function_derivative, starting_point, digits_of_precision):
    iteration_counter = 0

    f = function
    f_d = function_derivative

    x = starting_point

    while True:
        if f(x) == 0:
            return x, iteration_counter
        else:
            iteration_counter += 1
            x_next = x - f(x) / f_d(x)

            if abs(x_next - x) < 0.5 * 10 ** (-1.0 * digits_of_precision):
                return x_next, iteration_counter
            else:
                x = x_next


def classic_secant(function, point_one, point_two, digits_of_precision):
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


def f(x):
    return 94 * (cos(x) ** 3) - 24 * cos(x) + 177 * (sin(x) ** 2) - 108 * (sin(x) ** 4) - 72 * (cos(x) ** 3) * (sin(x) ** 2) - 65


def f_derivative(x):
    return - 282 * (cos(x) ** 2) * sin(x) + 24 * sin(x) + 354 * sin(x) * cos(x) - 432 * (sin(x) ** 3) * cos(x) + 216 * (cos(x) ** 2) * (sin(x) ** 3) - 144 * (cos(x) ** 4) * sin(x)


def f_second_derivative(x):
    return 564 * cos(x) * (sin(x) ** 2) - 282 * (cos(x) ** 3) + 24 * cos(x) + 354 * (cos(x) ** 2) - 354 * (sin(x) ** 2) - 1296 * (cos(x) ** 2) * (sin(x) ** 2) + 432 * (sin(x) ** 4) - 432 * cos(x) * (sin(x) ** 4) \
           + 648 * (cos(x) ** 3) * (sin(x) ** 2) + 576 * (cos(x) ** 3) * (sin(x) ** 2) - 144 * (cos(x) ** 5)


print("Bisection Comparison:\n")
print("Classic Bisection:")

root, loops_counter = classic_bisection(f, 0.8, 1.0, 5)
print("\tThe root in [0.8, 1.0]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = classic_bisection(f, 1.0, 1.2, 5)
print("\tThe root in [1.0, 1.2]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = classic_bisection(f, 2.2, 2.4, 5)
print("\tThe root in [2.2, 2.4]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

print("Modified Bisection:")
root, loops_counter = modified_bisection(f, 0.8, 1.0, 5)
print("\tThe root in [0.8, 1.0]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_bisection(f, 1.0, 1.2, 5)
print("\tThe root in [1.0, 1.2]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_bisection(f, 2.2, 2.4, 5)
print("\tThe root in [2.2, 2.4]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

print("---------------------------------------------------------------------------")

print("Newton-Raphson Comparison:\n")

print("Classic Newton-Raphson:")
root, loops_counter = classic_newton_raphson(f, f_derivative, 0.8, 5)
print("\tThe root near 0.8: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = classic_newton_raphson(f, f_derivative, 1.0, 5)
print("\tThe root near 1.0: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = classic_newton_raphson(f, f_derivative, 2.3, 5)
print("\tThe root near 2.3: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

print("Modified Newton-Raphson:")
root, loops_counter = modified_newton_raphson(f, f_derivative, f_second_derivative, 0.8, 5)
print("\tThe root near 0.8: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_newton_raphson(f, f_derivative, f_second_derivative, 1.0, 5)
print("\tThe root near 1.0: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_newton_raphson(f, f_derivative, f_second_derivative, 2.3, 5)
print("\tThe root near 2.3: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

print("---------------------------------------------------------------------------")

print("\nSecant Comparison:\n")
print("Classic Secant:")
root, loops_counter = classic_secant(f, 0.8, 0.9, 5)
print("\tThe root in [0.8, 0.9]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = classic_secant(f, 1.0, 1.2, 5)
print("\tThe root in [1.0, 1.2]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = classic_secant(f, 2.0, 2.5, 5)
print("\tThe root in [2.0, 2.5]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

print("Modified Secant:")
root, loops_counter = modified_secant(f, 0.8, 0.85, 0.9, 5)
print("\tThe root in [0.8, 0.9]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_secant(f, 1.0, 1.1, 1.2, 5)
print("\tThe root in [1.0, 1.2]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = modified_secant(f, 2.0, 2.25, 2.5, 5)
print("\tThe root in [2.0, 2.5]: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))
