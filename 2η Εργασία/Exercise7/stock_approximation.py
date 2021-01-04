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


def main():
    print("Results for ELL stock:\n")

    ELL_stock = [
        [0, 13.5600],
        [1, 13.1600],
        [2, 13.4000],
        [3, 13.3400],
        [4, 13.2800],
        [5, 13.3600],
        [6, 13.1400],
        [7, 13.2200],
        [8, 13.0000],
        [9, 13.2000],
    ]
    ELL_stock_dates = [
        [18, 9, 2020],
        [21, 9, 2020],
        [22, 9, 2020],
        [23, 9, 2020],
        [24, 9, 2020],
        [25, 9, 2020],
        [28, 9, 2020],
        [29, 9, 2020],
        [30, 9, 2020],
        [1, 10, 2020]
    ]

    print("-------Second degree polynomial results-------\n")

    ELL_2nd_degree_approximation_coefficients = approximate_function_with_least_squares(ELL_stock, 2)

    max_absolute_prediction_error = -1

    print("Close predictions of given data:")
    for i in range(len(ELL_stock)):
        approximate_value = calculate_polynomial(ELL_2nd_degree_approximation_coefficients, i)
        absolute_prediction_error = abs(ELL_stock[i][1] - approximate_value)

        if absolute_prediction_error > max_absolute_prediction_error:
            max_absolute_prediction_error = absolute_prediction_error

        print(
            "\tDate {:d}/{:d}/{:d}: predicted {:f}, was actually {:f}, with difference absolute error = {:f}".format(
                ELL_stock_dates[i][0], ELL_stock_dates[i][1], ELL_stock_dates[i][2], approximate_value, ELL_stock[i][1],
                absolute_prediction_error
            ))
    print("Maximum absolute prediction error is {:f}\n".format(max_absolute_prediction_error))

    print("Prediction of birthday close:")
    approximate_value = calculate_polynomial(ELL_2nd_degree_approximation_coefficients, 10)
    print("\tPrediction of stock in 2/10/2020 : {:f}, with actual value being: {:f} and absolute error {:f}".format(
        approximate_value, 13.2000, abs(13.2000 - approximate_value)
    ))
    print()

    print("Close prediction five days beyond given data: {:f}".format(
        calculate_polynomial(ELL_2nd_degree_approximation_coefficients, 15)))
    print()

    print("-------Third degree polynomial results-------\n")

    ELL_3rd_degree_approximation_coefficients = approximate_function_with_least_squares(ELL_stock, 3)

    max_absolute_prediction_error = -1
    print("Close predictions of given data:")
    for i in range(len(ELL_stock)):
        approximate_value = calculate_polynomial(ELL_3rd_degree_approximation_coefficients, i)
        absolute_prediction_error = abs(ELL_stock[i][1] - approximate_value)

        if absolute_prediction_error > max_absolute_prediction_error:
            max_absolute_prediction_error = absolute_prediction_error

        print(
            "\tDate {:d}/{:d}/{:d}: predicted {:f}, was actually {:f}, with difference absolute error = {:f}".format(
                ELL_stock_dates[i][0], ELL_stock_dates[i][1], ELL_stock_dates[i][2], approximate_value, ELL_stock[i][1],
                absolute_prediction_error
            ))
    print("Maximum absolute prediction error is {:f}\n".format(max_absolute_prediction_error))

    print("Prediction of birthday close:")
    approximate_value = calculate_polynomial(ELL_3rd_degree_approximation_coefficients, 10)
    print("\tPrediction of stock in 2/10/2020 : {:f}, with actual value being: {:f} and absolute error {:f}".format(
        approximate_value, 13.2000, abs(13.2000 - approximate_value)
    ))
    print()

    print("Close prediction five days beyond given data: {:f}".format(
        calculate_polynomial(ELL_3rd_degree_approximation_coefficients, 15)))
    print()

    print("-------Fourth degree polynomial results-------\n")

    ELL_4th_degree_approximation_coefficients = approximate_function_with_least_squares(ELL_stock, 4)

    max_absolute_prediction_error = -1
    print("Close predictions of given data:")
    for i in range(len(ELL_stock)):
        approximate_value = calculate_polynomial(ELL_4th_degree_approximation_coefficients, i)
        absolute_prediction_error = abs(ELL_stock[i][1] - approximate_value)

        if absolute_prediction_error > max_absolute_prediction_error:
            max_absolute_prediction_error = absolute_prediction_error

        print(
            "\tDate {:d}/{:d}/{:d}: predicted {:f}, was actually {:f}, with difference absolute error = {:f}".format(
                ELL_stock_dates[i][0], ELL_stock_dates[i][1], ELL_stock_dates[i][2], approximate_value, ELL_stock[i][1],
                absolute_prediction_error
            ))
    print("Maximum absolute prediction error is {:f}\n".format(max_absolute_prediction_error))

    print("Prediction of birthday close:")
    approximate_value = calculate_polynomial(ELL_4th_degree_approximation_coefficients, 10)
    print("\tPrediction of stock in 2/10/2020 : {:f}, with actual value being: {:f} and absolute error {:f}".format(
        approximate_value, 13.2000, abs(13.2000 - approximate_value)
    ))
    print()

    print("Close prediction five days beyond given data: {:f}".format(
        calculate_polynomial(ELL_4th_degree_approximation_coefficients, 15)))
    print()

    print("\n=======================")
    print("Results for ELIN stock:")
    print("=======================\n")

    ELIN_stock = [
        [0, 1.4500],
        [1, 1.5100],
        [2, 1.5100],
        [3, 1.4100],
        [4, 1.3700],
        [5, 1.3700],
        [6, 1.4100],
        [7, 1.4100],
        [8, 1.4100],
        [9, 1.4700],
    ]
    ELIN_stock_dates = [
        [18, 9, 2020],
        [21, 9, 2020],
        [22, 9, 2020],
        [23, 9, 2020],
        [24, 9, 2020],
        [25, 9, 2020],
        [28, 9, 2020],
        [29, 9, 2020],
        [30, 9, 2020],
        [1, 10, 2020]
    ]

    print("-------Second degree polynomial results-------\n")

    ELIN_2nd_degree_approximation_coefficients = approximate_function_with_least_squares(ELIN_stock, 2)

    max_absolute_prediction_error = -1
    print("Close predictions of given data:")
    for i in range(len(ELIN_stock)):
        approximate_value = calculate_polynomial(ELIN_2nd_degree_approximation_coefficients, i)
        absolute_prediction_error = abs(ELIN_stock[i][1] - approximate_value)

        if absolute_prediction_error > max_absolute_prediction_error:
            max_absolute_prediction_error = absolute_prediction_error

        print(
            "\tDate {:d}/{:d}/{:d}: predicted {:f}, was actually {:f}, with difference absolute error = {:f}".format(
                ELIN_stock_dates[i][0], ELIN_stock_dates[i][1], ELIN_stock_dates[i][2], approximate_value, ELIN_stock[i][1],
                absolute_prediction_error
            ))
    print("Maximum absolute prediction error is {:f}\n".format(max_absolute_prediction_error))

    print("Prediction of birthday close:")
    approximate_value = calculate_polynomial(ELIN_2nd_degree_approximation_coefficients, 10)
    print("\tPrediction of stock in 2/10/2020 : {:f}, with actual value being: {:f} and absolute error {:f}".format(
        approximate_value, 1.4700, abs(1.4700 - approximate_value)
    ))
    print()

    print("Close prediction five days beyond given data: {:f}".format(
        calculate_polynomial(ELIN_2nd_degree_approximation_coefficients, 15)))
    print()

    print("-------Third degree polynomial results-------\n")

    ELIN_3rd_degree_approximation_coefficients = approximate_function_with_least_squares(ELIN_stock, 3)

    max_absolute_prediction_error = -1
    print("Close predictions of given data:")
    for i in range(len(ELIN_stock)):
        approximate_value = calculate_polynomial(ELIN_3rd_degree_approximation_coefficients, i)
        absolute_prediction_error = abs(ELIN_stock[i][1] - approximate_value)

        if absolute_prediction_error > max_absolute_prediction_error:
            max_absolute_prediction_error = absolute_prediction_error

        print(
            "\tDate {:d}/{:d}/{:d}: predicted {:f}, was actually {:f}, with difference absolute error = {:f}".format(
                ELIN_stock_dates[i][0], ELIN_stock_dates[i][1], ELIN_stock_dates[i][2], approximate_value, ELIN_stock[i][1],
                absolute_prediction_error
            ))
    print("Maximum absolute prediction error is {:f}\n".format(max_absolute_prediction_error))

    print("Prediction of birthday close:")
    approximate_value = calculate_polynomial(ELIN_3rd_degree_approximation_coefficients, 10)
    print("\tPrediction of stock in 2/10/2020 : {:f}, with actual value being: {:f} and absolute error {:f}".format(
        approximate_value, 1.4700, abs(1.4700 - approximate_value)
    ))
    print()

    print("Close prediction five days beyond given data: {:f}".format(
        calculate_polynomial(ELIN_3rd_degree_approximation_coefficients, 15)))
    print()

    print("-------Fourth degree polynomial results-------\n")

    ELIN_4th_degree_approximation_coefficients = approximate_function_with_least_squares(ELIN_stock, 4)

    max_absolute_prediction_error = -1
    print("Close predictions of given data:")
    for i in range(len(ELIN_stock)):
        approximate_value = calculate_polynomial(ELIN_4th_degree_approximation_coefficients, i)
        absolute_prediction_error = abs(ELIN_stock[i][1] - approximate_value)

        if absolute_prediction_error > max_absolute_prediction_error:
            max_absolute_prediction_error = absolute_prediction_error

        print(
            "\tDate {:d}/{:d}/{:d}: predicted {:f}, was actually {:f}, with difference absolute error = {:f}".format(
                ELIN_stock_dates[i][0], ELIN_stock_dates[i][1], ELIN_stock_dates[i][2], approximate_value, ELIN_stock[i][1],
                absolute_prediction_error
            ))
    print("Maximum absolute prediction error is {:f}\n".format(max_absolute_prediction_error))

    print("Prediction of birthday close:")
    approximate_value = calculate_polynomial(ELIN_4th_degree_approximation_coefficients, 10)
    print("\tPrediction of stock in 2/10/2020 : {:f}, with actual value being: {:f} and absolute error {:f}".format(
        approximate_value, 1.4700, abs(1.4700 - approximate_value)
    ))
    print()

    print("Close prediction five days beyond given data: {:f}".format(
        calculate_polynomial(ELIN_4th_degree_approximation_coefficients, 15)))
    print()


if __name__ == '__main__':
    main()
