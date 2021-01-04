from math import sin, pi, sqrt
from random import uniform

from matplotlib import pyplot as plt


def polynomial_approximate(function_points):
    x = []
    y = []

    for x_y in function_points:
        x.append(x_y[0])
        y.append(x_y[1])

    sort_xy_pairs(x, y)

    dd = []

    temp_dd = []
    for i in range(1, len(function_points)):
        temp_dd.append((y[i] - y[i - 1]) / (x[i] - x[i - 1]))

    dd.append(temp_dd)

    for i in range(2, len(function_points)):
        temp_dd = []

        previous_dd = dd[i - 2]

        for j in range(len(function_points) - i):
            temp_dd.append((previous_dd[j + 1] - previous_dd[j]) / (x[i + j] - x[j]))

        dd.append(temp_dd)

    x_coefficients = [0 for i in range(len(function_points))]

    x_coefficients[0] = y[0]

    x_minus_xi_coefficients = [0 for i in range(len(function_points))]
    x_minus_xi_coefficients[0] = 1

    for i in range(1, len(x)):
        x_minus_xi_coefficients_new = [0 for i in range(len(x_minus_xi_coefficients))]

        for j in range(1, len(x_minus_xi_coefficients)):
            x_minus_xi_coefficients_new[j] = x_minus_xi_coefficients[j - 1]

        for j in range(len(x_coefficients)):
            x_minus_xi_coefficients_new[j] -= x_minus_xi_coefficients[j] * x[i - 1]

        x_minus_xi_coefficients = x_minus_xi_coefficients_new

        for j in range(len(x_coefficients)):
            x_coefficients[j] += x_minus_xi_coefficients[j] * dd[i - 1][0]

    return x_coefficients


def sort_xy_pairs(x, y):
    for i in range(len(x)):
        minimum = i
        for j in range(i, len(x)):
            if x[j] < x[minimum]:
                minimum = j

        temp = x[minimum]
        x[minimum] = x[i]
        x[i] = temp

        temp = y[minimum]
        y[minimum] = y[i]
        y[i] = temp


def calculate_polynomial(coefficients, x):
    x_power = 1

    result = 0

    for c in coefficients:
        result += c * x_power
        x_power *= x

    return result


def main():
    sin_training_points = [
        [-pi, 0],
        [-(7 / 9) * pi, -0.642788],
        [-(5 / 9) * pi, -0.984808],
        [-pi / 3, -0.866025],  # -sqrt(3) / 2
        [-pi / 9, -0.342020],
        [pi / 9, 0.342020],
        [pi / 3, 0.866025],  # sqrt(3) / 2
        [(5 / 9) * pi, 0.984808],
        [(7 / 9) * pi, 0.642788],
        [pi, 0]
    ]

    p_coefficients = polynomial_approximate(sin_training_points)

    print("p(x) = ", "{:f}".format(p_coefficients[0]), end="")
    print(" + {:f}x".format(p_coefficients[1]), end="")
    for i in range(2, len(p_coefficients) - 1):
        print(" + {:f}x^{:d}".format(p_coefficients[i], i), end=" ")
    print(" + {:f}x^{:d}".format(p_coefficients[len(p_coefficients) - 1], len(p_coefficients) - 1))

    x_points = []
    y_difference_values = []

    step = 2 * pi / 200
    target = -pi
    for i in range(200):
        x_points.append(target)
        y_difference_values.append(abs(calculate_polynomial(p_coefficients, target) - sin(target)))
        target += step

    plt.scatter(x_points, y_difference_values, s=1)
    plt.show()


if __name__ == '__main__':
    main()
