def vector_subtraction(lhs_vector, rhs_vector):
    lhs_copy = []
    for i in range(len(lhs_vector)):
        lhs_copy.append(lhs_vector[i])

    for i in range(len(lhs_copy)):
        lhs_copy[i] -= rhs_vector[i]

    return lhs_copy


def max_norm(vector):
    max_element = abs(vector[0])

    for i in vector:
        if abs(i) > max_element:
            max_element = abs(i)

    return max_element


def gauss_seidel(A, b, initial_guess, digits_of_precision):
    x_old = [i for i in initial_guess]
    while True:
        x = x_old.copy()

        for i in range(len(x)):
            x[i] = b[i]

            for j in range(i):
                x[i] -= A[i][j] * x[j]

            for j in range(i + 1, len(x)):
                x[i] -= A[i][j] * x[j]

            x[i] = x[i] / A[i][i]

        if max_norm(vector_subtraction(x, x_old)) < 0.5 * (10 ** (-1 * digits_of_precision)):
            return x
        else:
            x_old = x


if __name__ == '__main__':
    n = 100

    A = [[0 for it in range (n)] for itj in range (n)]

    B = [3]
    for i in range(n-2):
        B.append(1)
    B.append(3)

    for i in range(n-1):
        A[i][i] = 5
        A[i + 1][i] = A[i][i + 1] = -2
    A[n - 1][n - 1] = 5

    begin_x = [1.5 for i in range(len(A))]

    solution = gauss_seidel(A, B, begin_x, 4)

    print("Solution for n =", n)
    for position, i in enumerate(solution):
        print("b[", position + 1 , "]= ", i, sep="")

    n = 10000

    A = [[0 for it in range (n)] for itj in range (n)]

    B = [3]
    for i in range(n-2):
        B.append(1)
    B.append(3)

    for i in range(n-1):
        A[i][i] = 5
        A[i + 1][i] = A[i][i + 1] = -2
    A[n - 1][n - 1] = 5

    begin_x = [1.5 for i in range(len(A))]

    solution = gauss_seidel(A, B, begin_x, 4)

    print("Solution for n =", n)
    for position, i in enumerate(solution):
        print("b[", position + 1, "]= ", i, sep="")
