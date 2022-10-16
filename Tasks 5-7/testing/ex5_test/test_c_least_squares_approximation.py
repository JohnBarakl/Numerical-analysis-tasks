from unittest import TestCase

from Exercise5.c_least_squares_approximation import matrix_transposition, matrix_multiplication, least_squares, \
    calculate_polynomial, approximate_function_with_least_squares


class Test(TestCase):
    def test_least_squares(self):
        A = [
            [1, 1],
            [1, -1],
            [1, 1]
        ]

        b = [2, 1, 3]

        solution = least_squares(A, b)

        given_solution = [7 / 4, 3 / 4]

        with self.subTest():
            for i in range(len(solution)):
                self.assertAlmostEqual(given_solution[i], solution[i])

    def test_approximate_function_with_least_squares(self):
        test_points = [
            [-3, -1.4],
            [-2, 0],
            [0, 1.2],
            [1, 5.5],
            [4, 7],
            [6, 9]
        ]

        result = approximate_function_with_least_squares(test_points, 1)

        given_result = [1.17333, 2.37667]
        given_result.reverse()

        with self.subTest():
            self.assertAlmostEqual(given_result[0], round(result[0], 5))
        with self.subTest():
            self.assertAlmostEqual(given_result[1], round(result[1], 5))

    def test_approximate_function_with_least_squares3(self):
        test_points = [
            [-4.2, 10],
            [-3.6, 7],
            [-2.3, 13],
            [-1.8, 11],
            [-1.1, 9],
            [-0.4, 12],
            [0.6, 8],
            [1.2, 11]
        ]

        result = approximate_function_with_least_squares(test_points, 1)

        given_result = [0.151099, 10.3441]
        given_result.reverse()

        with self.subTest():
            self.assertAlmostEqual(given_result[0], round(result[0], 4))
        with self.subTest():
            self.assertAlmostEqual(given_result[1], round(result[1], 6))

    def test_approximate_function_with_least_squares2(self):
        test_points = [
            [1, 2],
            [-1, 1],
            [1, 3]
        ]

        result = approximate_function_with_least_squares(test_points, 1)

        given_result = [3 / 4, 7 / 4]
        given_result.reverse()

        with self.subTest():
            self.assertAlmostEqual(given_result[0], result[0])
        with self.subTest():
            self.assertAlmostEqual(given_result[1], result[1])

    def test_approximate_function_with_least_squares4(self):
        test_points = [
            [-1, 1],
            [0, 0],
            [1, 0],
            [2, -2]
        ]

        result = approximate_function_with_least_squares(test_points, 1)

        p_coefficients = result

        print("p(x) = ", "{:f}".format(p_coefficients[0]), end="")
        print(" + {:f}x".format(p_coefficients[1]), end="")
        for i in range(2, len(p_coefficients) - 1):
            print(" + {:f}x^{:d}".format(p_coefficients[i], i), end=" ")
        print(" + {:f}x^{:d}".format(p_coefficients[len(p_coefficients) - 1], len(p_coefficients) - 1))

        given_result = [0.2, -0.9]

        with self.subTest():
            self.assertAlmostEqual(given_result[0], result[0])
        with self.subTest():
            self.assertAlmostEqual(given_result[1], result[1])

    def test_approximate_function_with_least_squares5(self):
        test_points = [
            [-1, 1],
            [0, 0],
            [1, 0],
            [2, -2]
        ]

        result = approximate_function_with_least_squares(test_points, 2)

        given_result = [0.45, -0.65, -0.25]

        with self.subTest():
            self.assertAlmostEqual(given_result[0], result[0])
        with self.subTest():
            self.assertAlmostEqual(given_result[1], result[1])
        with self.subTest():
            self.assertAlmostEqual(given_result[2], result[2])

    def test_matrix_transposition(self):
        mat = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        given_matT = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]

        matT = matrix_transposition(mat)

        for i in range(len(mat)):
            for j in range(len(mat)):
                with self.subTest():
                    self.assertEqual(given_matT[i][j], matT[i][j])

    def test_matrix_transposition2(self):
        mat = [
            [5, 2, 3],
            [4, 5, 6],
            [7, 8, 5]
        ]

        given_matT = [
            [5, 4, 7],
            [2, 5, 8],
            [3, 6, 5]
        ]

        matT = matrix_transposition(mat)

        for i in range(len(mat)):
            for j in range(len(mat)):
                with self.subTest():
                    self.assertEqual(given_matT[i][j], matT[i][j])

    def test_matrix_transposition3(self):
        mat = [
            [5, 2, 9],
            [4, 1, 6],
            [3, 8, 5]
        ]

        given_matT = [
            [5, 4, 3],
            [2, 1, 8],
            [9, 6, 5]
        ]

        matT = matrix_transposition(mat)

        for i in range(len(mat)):
            for j in range(len(mat)):
                with self.subTest():
                    self.assertEqual(given_matT[i][j], matT[i][j])

    def test_matrix_transposition4(self):
        mat = [
            [1, 2, 3],
            [4, 5, 6]
        ]

        given_matT = [
            [1, 4],
            [2, 5],
            [3, 6]
        ]

        matT = matrix_transposition(mat)

        for i in range(len(mat)):
            for j in range(len(mat)):
                with self.subTest():
                    self.assertEqual(given_matT[i][j], matT[i][j])

    def test_matrix_transposition5(self):
        mat = [
            [1, -3, -5]
        ]

        given_matT = [
            [1],
            [-3],
            [-5]
        ]

        matT = matrix_transposition(mat)

        for i in range(len(mat)):
            for j in range(len(mat)):
                with self.subTest():
                    self.assertEqual(given_matT[i][j], matT[i][j])

    def test_matrix_multiplication(self):
        m1 = [
            [7, -4, 5]
        ]
        m2 = [
            [3],
            [2],
            [-1]
        ]

        result = [[8.0]]

        self.assertListEqual(result, matrix_multiplication(m1, m2))

    def test_matrix_multiplication2(self):
        m1 = [
            [6, -1, 8, 3]
        ]
        m2 = [
            [4],
            [-9],
            [-2],
            [5]
        ]

        result = [
            [32.0]
        ]

        self.assertListEqual(result, matrix_multiplication(m1, m2))

    def test_matrix_multiplication3(self):
        m1 = [
            [1, 3],
            [2, -1]
        ]
        m2 = [
            [2, 0, -4],
            [5, -2, 6]
        ]

        result = [
            [17.0, -6.0, 14.0],
            [-1.0, 2.0, -14.0]
        ]

        self.assertListEqual(result, matrix_multiplication(m1, m2))

    def test_matrix_multiplication4(self):
        m1 = [
            [1, 2],
            [3, 4]
        ]
        m2 = [
            [5, 6],
            [0, -2]
        ]

        with self.subTest():
            result = [
                [5.0, 2.0],
                [15.0, 10.0]
            ]

            self.assertListEqual(result, matrix_multiplication(m1, m2))

        with self.subTest():
            result = [
                [23.0, 34.0],
                [-6.0, -8.0]
            ]

            self.assertListEqual(result, matrix_multiplication(m2, m1))
