import math
from math import sin
from math import e


def f(x):
    return e ** (sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1 # Ορισμός της f(x)


def bisection(function, range_beginning, range_ending, digits_of_precision):
    f = function
    a = range_beginning
    b = range_ending
    fa = f(a)
    fb = f(b)

    m = (a+b)/2
    fm = f(m)

    while True:
        if fm == 0:
            return m
        elif fa * fm < 0:
            fb = fm
            b = m
        else:
            fa = fm
            a = m

        old_m = m
        m = (a + b) / 2
        fm = f(m)

        if abs(old_m - m) < 0.5*(10**(-1 * digits_of_precision)):
            return m


print("Η ρίζα στο διάστημα [-2, -0.5]: ", bisection(f, -2, -0.5, 5))
print("Η ρίζα στο διάστημα [-0.5,0.5]: ", bisection(f, -0.5, 0.5, 5))
print("Η ρίζα στο διάστημα [0.5, 2]: ", bisection(f, 0.5, 2, 5))

