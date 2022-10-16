from math import pi, sin
from unittest import TestCase

from Exercise5.b_splines_approximation import splines_approximate, calculate_spline, solve_system


class Test(TestCase):
    def test_splines_approximate1(self):
        test_points = [
            [-1, 0],
            [0, 2],
            [1, 6]
        ]

        testRes = (splines_approximate(test_points))

        for i in test_points:
            print()
            self.assertAlmostEqual(calculate_spline(testRes, i[0]), i[1],
                                   msg="f({0:f}) = {1:f} != {2:f} = s({0:f})".format(i[0], i[1],

                                                                                     calculate_spline(testRes, i[0])))
    def test_splines_approximate2(self):
        sin_training_points = []

        x = -pi

        for i in range(10):
            sin_training_points.append([])
            sin_training_points[i].append(x)
            sin_training_points[i].append(round(sin(x), 6))
            x += 2 * pi / 9
            x = round(x, 6)

        test_points = sin_training_points

        testRes = (splines_approximate(test_points))

        for i in test_points:
            print()
            self.assertAlmostEqual(calculate_spline(testRes, i[0]), i[1],
                                   msg="f({0:f}) = {1:f} != {2:f} = s({0:f})".format(i[0], i[1],

                                                                                     calculate_spline(testRes, i[0])))
    # def test_system_solver(self):
    #     A = [
    #         [2, -3, 1],
    #         [3, 1, -1],
    #         [1, -1, -1]
    #     ]
    #
    #     b = [1, 2, 1]
    #
    #     x = solve_system(A, b)
    #
    #     x_given = [4 / 7, -1 / 14, -5 / 14]
    #
    #     for i in range(len(b)):
    #         self.assertAlmostEqual(x[i], x_given[i])
    #
    # def test_system_solver2(self):
    #     A = [
    #         [1, -5, 1],
    #         [2, 4, 1],
    #         [1, 1, 1]
    #     ]
    #
    #     b = [2, 1, 0]
    #
    #     x = solve_system(A, b)
    #
    #     x_given = [2, -1 / 3, -5 / 3]
    #
    #     for i in range(len(b)):
    #         self.assertAlmostEqual(x[i], x_given[i])
    #
    # def test_system_solver3(self):
    #     A = [
    #         [4, 3, 4],
    #         [9, 3, 4],
    #         [1, 1, 1]
    #     ]
    #
    #     b = [8, 7, 3]
    #
    #     x = solve_system(A, b)
    #
    #     x_given = [-1 / 5, 4, -4 / 5]
    #
    #     for i in range(len(b)):
    #         print(x[i], x_given[i], x[i] - x_given[i])
    #         self.assertAlmostEqual(x[i], x_given[i])
    #
    # def test_system_solver4(self):
    #     A = [
    #         [1, -1, 3],
    #         [-1, 0, -2],
    #         [2, 2, 4]
    #     ]
    #
    #     b = [-3, 1, 0]
    #
    #     x = solve_system(A, b)
    #
    #     x_given = [1, 1, -1]
    #
    #     for i in range(len(b)):
    #         print(x[i], x_given[i], x[i] - x_given[i])
    #         self.assertAlmostEqual(x[i], x_given[i])
    #
    # def test_system_solver5(self):
    #     A = [
    #         [2, 1, 5],
    #         [4, 4, -4],
    #         [1, 3, 1]
    #     ]
    #
    #     b = [5, 0, 6]
    #
    #     x = solve_system(A, b)
    #
    #     x_given = [-1, 2, 1]
    #
    #     for i in range(len(b)):
    #         print(x[i], x_given[i], x[i] - x_given[i])
    #         self.assertAlmostEqual(x[i], x_given[i])
    #
    # def test_system_solver6(self):
    #     A = [
    #         [2, 3],
    #         [3, 2]
    #     ]
    #
    #     b = [4, 1]
    #
    #     x = solve_system(A, b)
    #
    #     x_given = [-1, 2]
    #
    #     for i in range(len(b)):
    #         print(x[i], x_given[i], x[i] - x_given[i])
    #         self.assertAlmostEqual(x[i], x_given[i])