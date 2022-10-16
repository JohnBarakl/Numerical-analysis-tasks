import random

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