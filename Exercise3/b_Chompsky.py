import math


def matrix_multiplication(lhs_matrix, rhs_matrix):
    result = [[0.0 for j in range(len(rhs_matrix[0]))] for i in range(len(lhs_matrix))]

    for i in range(len(lhs_matrix)):
        for k in range(len(rhs_matrix[0])):
            for j in range(len(rhs_matrix)):
                result[i][k] += lhs_matrix[i][j] * rhs_matrix[j][k]

    return result


def chompsky_update_submatrix(matrix, prev_diagonal_position):
    rest_of_column = []
    rest_of_column_transpose = [[]]
    for row in range(prev_diagonal_position + 1, len(matrix)):
        rest_of_column.append([matrix[row][prev_diagonal_position]])
        rest_of_column_transpose[0].append(matrix[row][prev_diagonal_position])

    submatrix_to_remove = matrix_multiplication(rest_of_column, rest_of_column_transpose)

    for i in range(0, len(submatrix_to_remove)):
        for j in range(0, len(submatrix_to_remove)):
            matrix[i + prev_diagonal_position + 1][j + prev_diagonal_position + 1] -= submatrix_to_remove[i][j]


def chompsky_core(matrix, diagonal_position):
    if (diagonal_position >= len(matrix)):
        return matrix

    matrix[diagonal_position][diagonal_position] = math.sqrt(matrix[diagonal_position][diagonal_position])
    for i in range(diagonal_position + 1, len(matrix)):
        matrix[i][diagonal_position] = matrix[i][diagonal_position] / matrix[diagonal_position][diagonal_position]
        matrix[diagonal_position][i] = 0

    chompsky_update_submatrix(matrix, diagonal_position)

    return chompsky_core(matrix, diagonal_position + 1)


def chompsky(matrix):
    return chompsky_core(matrix, 0)

m = chompsky(
    [
        [4, -2],
        [-2, 6]
    ]
)

for f in m:
    print(f)
