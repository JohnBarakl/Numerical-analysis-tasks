def vector_subtraction(lhs_vector, rhs_vector):
    lhs_copy = []
    for i in range(len(lhs_vector)):
        lhs_copy.append(i)

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

        if max_norm(vector_subtraction(x, x_old)) < 0.5 * (10 ** -4):
            return x
        else:
            x_old = x


n = 10

testA = [[0 for it in range (n)] for itj in range (n) ]

testB = [3]
for i in range(n-2):
    testB.append(1)
testB.append(3)

for i in range(n-1):
    testA[i][i] = 5
    testA[i+1][i] = testA[i][i+1] = -2
testA[n-1][n-1] = 5

begin_x = [0.0 for i in range(len(testA))]

solution = gauss_seidel(testA, testB, begin_x, 4)

for i in solution:
    print(i)
