from Exercise2.b_Modified_Bisection import modified_bisection

import math
from math import sin, cos

def f(x):
    return 94 * (cos(x) ** 3) - 24 * cos(x) + 177 * (sin(x) ** 2) - 108 * (sin(x) ** 4) - 72 * (cos(x) ** 3) * (sin(x) ** 2) - 65


print("First root:")
for i in range(10):
    root, loops_counter = modified_bisection(f, 0.8, 1.0, 5)
    print("\tRoot: {:f} calculated in {:d} repetitions".format(root, loops_counter))

print("Second root:")
for i in range(10):
    root, loops_counter = modified_bisection(f, 1.0, 1.2, 5)
    print("\tRoot: {:f} calculated in {:d} repetitions".format(root, loops_counter))

print("Third root:")
for i in range(10):
    root, loops_counter = modified_bisection(f, 2.2, 2.4, 5)
    print("\tRoot: {:f} calculated in {:d} repetitions".format(root, loops_counter))
