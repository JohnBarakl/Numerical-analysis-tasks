import math
from math import sin
from math import e


def f(x):
    return e ** (sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1 # Ορισμός της f(x)


def bisection(function, rangeBeginning, rangeEnding, digitsOfPrecision):
    f = function
    a = rangeBeginning
    b = rangeEnding
    fa = f(a)
    fb = f(b)

    oldM = 0
    m = (a+b)/2
    fm = f(m)

    while math.fabs(oldM - m) >= 0.5*(10**(-1*digitsOfPrecision)):

        if fm == 0:
            return m
        elif fa * fm < 0:
            fb = fm
            b = m
        else:
            fa = fm
            a = m

        oldM = m
        m = (a + b) / 2
        fm = f(m)

    return m



print(round(bisection(f, -1.5, -1, 5)),5)

