from .b_Modified_Bisection import modified_bisection
from .a_Modified_Newton_Raphson import modified_newton_raphson

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
