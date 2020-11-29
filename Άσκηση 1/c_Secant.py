import math
from math import sin
from math import e


def f(x):
    return e ** (sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1  # Ορισμός της f(x)


def secant(function, range_beginning, range_ending, digits_of_precision):
    iteration_counter = 0

    f = function

    x1 = range_beginning  # Θεωρώ ως πρώτο σημείο την το αριστερό άκρο του διαστήματος
    x2 = range_ending  # Θεωρώ ως δεύτερο σημείο την το δεξί άκρο του διαστήματος

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


root, loops_counter = secant(f, -2, -1, 5)
print("Η ρίζα στο διάστημα [-2, -1]: {:f} που υπολογίστηκε σε {:d} επαναλήψεις".format(root, loops_counter))

root, loops_counter = secant(f, -0.1, 0.1, 5)
print("Η ρίζα στο διάστημα [-0.5,0.5]: {:f} που υπολογίστηκε σε {:d} επαναλήψεις".format(root, loops_counter))

root, loops_counter = secant(f, 1.25, 2, 5)
print("Η ρίζα στο διάστημα [1.25, 2]: {:f} που υπολογίστηκε σε {:d} επαναλήψεις".format(root, loops_counter))

print(f(0.1))