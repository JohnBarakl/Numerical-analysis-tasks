import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin
from numpy import cos

x = np.arange(2.25, 2.35, 0.0001) # Η f(x) ορίζεται στο [-2,2]

fx = 94 * (cos(x) ** 3) - 24 * cos(x) + 177 * (sin(x) ** 2) - 108 * (sin(x) ** 4) - 72 * (cos(x) ** 3) * (sin(x) ** 2) - 65

fig, ax = plt.subplots()
ax.plot(x, fx)
ax.axhline(c="black")
ax.grid()
plt.title("Η γραφική παράσταση της $f(x) = 94cos^3x - 24cosx + 177sin^2x -108sin^4x - 72cos^3xsin^2x - 65$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
