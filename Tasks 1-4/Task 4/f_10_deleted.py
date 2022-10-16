def construct_G(A, q, n):
    google_matrix = [[0.0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            row_sum = 0
            for k in range(len(A[j])):
                row_sum += A[j][k]

            google_matrix[i][j] = ((q / n) + ((A[j][i] * (1 - q)) / row_sum))

    return google_matrix


def matrix_columnMatrix_multiplication(lhs_matrix, rhs_columnMatrix):
    result = [0.0 for i in range(len(rhs_columnMatrix))]

    for i in range(len(lhs_matrix)):
        for j in range(len(lhs_matrix[i])):
            result[i] += lhs_matrix[i][j] * rhs_columnMatrix[j]

    return result


def integer_columnMatrix_multiplication(integer, columnMatrix):
    result = []

    for element in columnMatrix:
        result.append(integer * element)

    return result


def power_method(matrix, digits_of_precision):
    p = [1/len(matrix) for i in range(len(matrix))]
    eigenvalue_estimate = 0

    while True:

        p_new = matrix_columnMatrix_multiplication(matrix, p)

        new_eigenvalue_estimate = 0
        for i in p_new:
            if i != 0:
                new_eigenvalue_estimate = i
                break

        if new_eigenvalue_estimate == 0:
            return p_new

        p_new = integer_columnMatrix_multiplication(1 / new_eigenvalue_estimate, p_new)

        if abs(new_eigenvalue_estimate - eigenvalue_estimate) < 0.5 * (10 ** (-1.0 * digits_of_precision)):
            return p_new

        else:
            p = p_new
            eigenvalue_estimate = new_eigenvalue_estimate


if __name__ == '__main__':

    A_modified = [
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    ]


    q = 0.15
    n = len(A_modified)

    G = construct_G(A_modified, q, n)

    p = power_method(G, 7)

    element_sum = 0
    for i in p:
        element_sum += i
    p = integer_columnMatrix_multiplication(1 / element_sum, p)

    print("\nNew rank matrix p: ")
    element_sum = 0
    for i in range(9):
        print("p[{:02d}]:".format(i + 1), round(p[i], 7))
        element_sum += p[i]
    for i in range(9, len(p)):
        print("p[{:02d}]:".format(i + 2), round(p[i], 7))
        element_sum += p[i]

    print("\nWith sum =", element_sum)

