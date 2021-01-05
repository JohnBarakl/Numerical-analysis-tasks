from math import sin, pi

from matplotlib import pyplot as plt


def least_squares(A, b):
    AT = matrix_transposition(A)

    AT_A = matrix_multiplication(AT, A)
    AT_b = matrix_vector_multiplication(AT, b)

    return solve_system(AT_A, AT_b)


def approximate_function_with_least_squares(function_points, polynomial_degree):
    A = [[0.0 for j in range(polynomial_degree + 1)] for i in range(len(function_points))]
    b = [0.0 for i in range(len(function_points))]

    for i in range(len(function_points)):
        for j in range(polynomial_degree + 1):
            A[i][j] = function_points[i][0] ** j
        b[i] = function_points[i][1]

    return least_squares(A, b)


def calculate_polynomial(coefficients, x):
    x_power = 1

    result = 0

    for c in coefficients:
        result += c * x_power
        x_power *= x

    return result


def matrix_multiplication(lhs_matrix, rhs_matrix):
    result = [[0.0 for j in range(len(rhs_matrix[0]))] for i in range(len(lhs_matrix))]

    for i in range(len(lhs_matrix)):
        for k in range(len(rhs_matrix[0])):
            for j in range(len(rhs_matrix)):
                result[i][k] += lhs_matrix[i][j] * rhs_matrix[j][k]

    return result


def matrix_transposition(matrix):
    transposed = [[0.0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transposed[j][i] = matrix[i][j]

    return transposed


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
    result = [0 for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
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


def sin_approximation(x):
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

    return calculate_polynomial(approximate_function_with_least_squares(sin_training_points, 2), x)


def main():
    x_points = []
    y_difference_values = []

    step = 2 * pi / 199
    current_x = -pi
    for i in range(200):
        x_points.append(current_x)
        y_difference_values.append(abs(sin_approximation(current_x) - sin(current_x)))
        current_x += step

    plt.scatter(x_points, y_difference_values, s=1)
    plt.title("Διάγραμμα απολύτου σφάλματος προσέγγισης")
    plt.xlabel("x")
    plt.ylabel("Απόλυτο σφάλμα προσέγγισης του ημιτόνου")
    plt.show()


if __name__ == '__main__':
    main()
