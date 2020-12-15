import math
from math import sin
from math import cos
from math import e


def f(x):
    return e ** (sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1  # Ορισμός της f(x)


def f_derivative(x):
    return 3 * (sin(x) ** 2) * cos(x) * (e ** (sin(x) ** 3)) + 6 * x ** 5 - 8 * x ** 3 - 3 * x ** 2  # Η παράγωγος της f(x)


def newton_raphson(function, function_derivative, starting_point, digits_of_precision):
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

root, loops_counter = newton_raphson(f, f_derivative, -1.5, 5)
print("The root near -1.5: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = newton_raphson(f, f_derivative, 0.6, 5)
print("The root near 0: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

root, loops_counter = newton_raphson(f, f_derivative, 1.75, 5)
print("The root near 1.75: {:f}. It was calculated in {:d} repetitions".format(root, loops_counter))

def fpp(x):
    return 9*e**(sin(x)**3)*(cos(x)**2)*(sin(x)**4)-3*e**(sin(x)**3)*(sin(x)**3)+6*e**(sin(x)**3)*(cos(x)**2)*sin(x)+30*x**4-24*x**2-6*x