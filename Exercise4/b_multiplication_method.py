import math


def matrix_vector_multiplication(lhs_matrix, rhs_vector):
    result = [0.0 for i in range(len(rhs_vector))]

    for i in range(len(lhs_matrix)):
        for j in range(len(lhs_matrix[i])):
            result[i] += lhs_matrix[i][j] * rhs_vector[j]

    return result


def integer_vector_multiplication(integer, vector):
    result = []

    for element in vector:
        result.append(integer * abs(element))

    return result


def vector_subtraction(v1, v2):
    temp = [i for i in v1]

    for i in range(len(temp)):
        temp[i] -= v2[i]

    return temp


def max_norm(vec):
    max = -1
    for i in vec:
        if abs(i) > max:
            max = abs(i)

    return max


def sum_matrix_row(matrix, row):
    sum = 0
    for j in range(len(matrix[row])):
        sum += matrix[row][j]

    return sum


def multiplication_method(matrix, digits_of_precision):
    p = [1/len(matrix) for i in range(len(matrix))]

    while True:

        p_new = matrix_vector_multiplication(matrix, p)

        eigenvalue_estimate = 0
        for i in p_new:
            if i != 0:
                eigenvalue_estimate = i
                break

        p_new = integer_vector_multiplication(1 / eigenvalue_estimate, p_new)

        if abs(eigenvalue_estimate - 1) < 0.5 * (10 ** (-1.0 * digits_of_precision)):
            sum = 0
            for i in p_new:
                sum += i

            return integer_vector_multiplication(1 / sum, p_new)

        else:
            p = p_new


print(__name__)
A = [
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
    ]

# A = [
#     [0, 1, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [0, 1, 0, 1, 1],
#     [1, 0, 1, 0, 1],
#     [0, 0, 0, 1, 0]
# ]

# A2 = [[0 for i in range(15)] for j in range(15)]
# A2[1-1][9-1] = 1
# A2[1-1][2-1] = 1
# A2[2-1][5-1] = 1
# A2[2-1][7-1] = 1
# A2[2-1][3-1] = 1
# A2[3-1][2-1] = 1
# A2[3-1][6-1] = 1
# A2[3-1][8-1] = 1
# A2[4-1][3-1] = 1
# A2[4-1][12-1] = 1
# A2[5-1][1-1] = 1
# A2[5-1][10-1] = 1
# A2[6-1][10-1] = 1
# A2[6-1][11-1] = 1
# A2[7-1][10-1] = 1
# A2[7-1][11-1] = 1
# A2[8-1][11-1] = 1
# A2[8-1][4-1] = 1
# A2[9-1][5-1] = 1
# A2[9-1][6-1] = 1
# A2[9-1][10-1] = 1
# A2[10-1][13-1] = 1
# A2[11-1][15-1] = 1
# A2[12-1][8-1] = 1
# A2[12-1][7-1] = 1
# A2[12-1][11-1] = 1
# A2[13-1][9-1] = 1
# A2[13-1][14-1] = 1
# A2[14-1][10-1] = 1
# A2[14-1][13-1] = 1
# A2[14-1][11-1] = 1
# A2[14-1][15-1] = 1
# A2[15-1][12-1] = 1
# A2[15-1][14-1] = 1

q = 0.15
n = len(A)

G = [[0.0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        G[i][j] = ( (q / n) + ((A[j][i] * (1 - q)) / sum_matrix_row(A, j)))

print("Sums of Google matrix's columns: ")
temp = 0
for i in range(len(G)):
    temp=0
    for j in range(len(G)):
        temp += G[j][i]
    print(temp, end="\t")
print()


r= multiplication_method(G, 7)

print("Probability vector p: ")
temp = 0
for i in r:
    print(round(i, 7))
    temp += i

print("\nWith sum =", temp)