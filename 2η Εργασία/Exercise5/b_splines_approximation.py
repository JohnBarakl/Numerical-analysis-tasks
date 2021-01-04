from math import sin, pi

from matplotlib import pyplot as plt

import numpy


def splines_approximate(function_points):
    coefficients_matrix = [[0 for j in range(4 * (len(function_points) - 1))] for i in
                           range(4 * (len(function_points) - 1))]
    constants_matrix = [0 for i in range(4 * (len(function_points) - 1))]

    equasion_row = 0

    for given_point_number in range(1, len(function_points)):
        for x_power in range(3, 0, -1):
            coefficients_matrix[equasion_row][3 - x_power + (given_point_number - 1) * 4] = \
            function_points[given_point_number - 1][0] ** x_power
            coefficients_matrix[equasion_row + 1][3 - x_power + (given_point_number - 1) * 4] = \
            function_points[given_point_number][0] ** x_power
        constants_matrix[equasion_row] = function_points[given_point_number - 1][1]
        constants_matrix[equasion_row + 1] = function_points[given_point_number][1]
        coefficients_matrix[equasion_row][3 + (given_point_number - 1) * 4] = 1
        coefficients_matrix[equasion_row + 1][3 + (given_point_number - 1) * 4] = 1

        equasion_row += 2

    for given_point_number in range(1, len(function_points) - 1):
        for x_power in range(2, 0, -1):
            coefficients_matrix[equasion_row][2 - x_power + (given_point_number - 1) * 4] = (function_points[
                                                                                                 given_point_number][
                                                                                                 0] ** x_power) * (
                                                                                                        x_power + 1)
            coefficients_matrix[equasion_row][2 - x_power + given_point_number * 4] = -1 * (
                        function_points[given_point_number][0] ** x_power) * (x_power + 1)
        coefficients_matrix[equasion_row][2 + (given_point_number - 1) * 4] = 1
        coefficients_matrix[equasion_row][2 + given_point_number * 4] = -1
        constants_matrix[equasion_row] = 0

        equasion_row += 1

    for given_point_number in range(1, len(function_points) - 1):
        coefficients_matrix[equasion_row][(given_point_number - 1) * 4] = function_points[given_point_number][0] * 6
        coefficients_matrix[equasion_row][given_point_number * 4] = -1 * function_points[given_point_number][0] * 6
        coefficients_matrix[equasion_row][1 + (given_point_number - 1) * 4] = 2
        coefficients_matrix[equasion_row][1 + given_point_number * 4] = -2
        constants_matrix[equasion_row] = 0

        equasion_row += 1

    coefficients_matrix[equasion_row][0] = function_points[0][0] * 6
    coefficients_matrix[equasion_row][1] = 2
    constants_matrix[equasion_row] = 0
    equasion_row += 1

    coefficients_matrix[equasion_row][(len(function_points) - 2) * 4] = function_points[len(function_points) - 1][0] * 6
    coefficients_matrix[equasion_row][1 + (len(function_points) - 2) * 4] = 2
    constants_matrix[equasion_row] = 0

    np_solve = numpy.linalg.solve(coefficients_matrix, constants_matrix)

    splines_coefficients_array = solve_system(coefficients_matrix, constants_matrix)
    splines_coefficients_matrix = []

    for i in range(0, len(function_points) - 1):
        x_coefficients = []
        x_range = [function_points[i][0], function_points[i + 1][0]]
        for j in range(4):
            x_coefficients.append(splines_coefficients_array[4 * i + j])
        splines_coefficients_matrix.append([x_range, x_coefficients])

    return splines_coefficients_matrix


def calculate_spline(spline_coefficients, x):
    for i in range(len(spline_coefficients)):
        if spline_coefficients[i][0][0] <= x <= spline_coefficients[i][0][1]:
            return spline_coefficients[i][1][0] * x ** 3 + spline_coefficients[i][1][1] * x ** 2 + \
                   spline_coefficients[i][1][2] * x + spline_coefficients[i][1][3]

    return None


def swap_rows(matrix, row1, row2):
    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp


def pivot_matrix(matrix, pivot, P):
    max_row_element_pos = pivot
    for i in range(pivot + 1, len(matrix)):
        if abs(matrix[i][pivot]) > abs(matrix[max_row_element_pos][pivot]):
            max_row_element_pos = i

    swap_rows(matrix, pivot, max_row_element_pos)
    swap_rows(P, pivot, max_row_element_pos)


def matrix_vector_multiplication(matrix, vector):
    result = [0 for i in range(len(vector))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[i] += matrix[i][j] * vector[j]

    return result


def PLU(A):
    P = []
    U = []
    for rowNumber, row in enumerate(A):
        U.append([])
        P.append([])
        for element in row:
            U[rowNumber].append(element)
            P[rowNumber].append(0)

    for r in range(len(U)):
        P[r][r] = 1

    for row_number in range(len(U) - 1):
        pivot_matrix(U, row_number, P)
        for other_row_num in range(row_number + 1, len(U)):
            U[other_row_num][row_number] = U[other_row_num][row_number] / U[row_number][row_number]
            for col_number in range(row_number + 1, len(U)):
                U[other_row_num][col_number] = U[other_row_num][col_number] - (U[other_row_num][row_number]) * \
                                               U[row_number][col_number]

    L = [[0 for i in range(len(U))] for j in range(len(U))]
    for i in range(len(U)):
        L[i][i] = 1
    for i in range(len(U)):
        for j in range(len(U)):
            if i > j:
                L[i][j] = U[i][j]
                U[i][j] = 0

    return P, L, U


def solve_system(A, b):
    P, L, U = PLU(A)

    Pb = matrix_vector_multiplication(P, b)

    y = [0.0 for i in range(len(Pb))]

    for i in range(len(L)):
        y[i] = Pb[i]
        for j in range(len(L)):
            if j == i:
                continue

            y[i] -= L[i][j] * y[j]
        y[i] = y[i] / L[i][i]

    x = [0.0 for i in range(len(y))]

    for i in range(len(U) - 1, -1, -1):
        x[i] = y[i]
        for j in range(len(U)):
            if j == i:
                continue

            x[i] -= U[i][j] * x[j]
        x[i] = x[i] / U[i][i]

    return x


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

    splines_coefficients = splines_approximate(sin_training_points)

    print("s(x) = ")
    for x_range, coefficients in splines_coefficients:
        print("\t {:f}x^3 + {:f}x^2 + {:f}x + {:f}".format(coefficients[0], coefficients[1], coefficients[2],
                                                           coefficients[3], ))
    print()

    x_points = []
    y_difference_values = []

    step = 2 * pi / 200
    target = -pi
    for i in range(200):
        x_points.append(target)
        y_difference_values.append(abs(calculate_spline(splines_coefficients, target) - sin(target)))
        target += step

    plt.scatter(x_points, y_difference_values, s=1)
    plt.show()


if __name__ == '__main__':
    main()
