import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2.0, 2.0, 0.001) # Η f(x) ορίζεται στο [-2,2]

fx = np.e ** (np.sin(x) ** 3) + x ** 6 - 2 * x ** 4 - x ** 3 - 1 # Ορισμός της f(x)

fig, ax = plt.subplots()
ax.plot(x, fx)
ax.grid()
ax.axhline(c="black")
plt.title("Η γραφική παράσταση της $f(x) = e^{sin^{3}x} + x^6 - 2x^4 - x^3 -1$")
plt.xlabel("x")
plt.ylabel("f(x)")


ax.annotate("Ρίζες",
            xy=(0, 0), xycoords='data',
            xytext=(-0.15, 5), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

ax.annotate("Ρίζες",
            xy=(-1.197624, 0), xycoords='data',
            xytext=(-0.15, 5), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

ax.annotate("Ρίζες",
            xy=(1.530134, 0), xycoords='data',
            xytext=(-0.15, 5), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

plt.show()
