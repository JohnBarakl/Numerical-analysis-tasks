import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin
from numpy import cos

x = np.arange(0, 3, 0.0001) # Η f(x) ορίζεται στο [0, 3]

fx = 94 * (cos(x) ** 3) - 24 * cos(x) + 177 * (sin(x) ** 2) - 108 * (sin(x) ** 4) - 72 * (cos(x) ** 3) * (sin(x) ** 2) - 65

fig, ax = plt.subplots()
ax.plot(x, fx)
ax.axhline(c="black")
ax.grid()
plt.title("Η γραφική παράσταση της $f$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
