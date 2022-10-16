from unittest import TestCase

from Exercise6 import a_simpson_integration, b_trapezoid_integration
from Exercise6.a_simpson_integration import simpson_integral_from_points
from Exercise6.b_trapezoid_integration import trapezoid_integral_from_points


class Test(TestCase):
    def test_simpson_sin_integral_from_points(self):
        chosen_points = [
            [0, 1],
            [0.125, 0.9844],
            [0.25, 0.9394],
            [0.375, 0.8688],
            [0.5, 0.7788],
            [0.625, 0.6766],
            [0.75, 0.5697],
            [0.875, 0.465],
            [1, 0.3678]
        ]

        self.assertAlmostEqual(0.7467, simpson_integral_from_points(chosen_points), 3)

    def test_simpson_sin_integral_from_points2(self):
        chosen_points = [
        ]

        x0 = 0
        for i in range(11):
            chosen_points.append([x0+0.1*i, (x0+0.1*i)**5])

        self.assertAlmostEqual(0.1667, simpson_integral_from_points(chosen_points), 4)

    def test_simpson_sin_integral_from_points3(self):
        chosen_points = [
        ]

        x0 = 0
        for i in range(11):
            chosen_points.append([x0+0.1*i, (x0+0.1*i)**4])

        self.assertAlmostEqual(0.200, simpson_integral_from_points(chosen_points), 4)

    def test_trapezoid_sin_integral_from_points(self):
        chosen_points = [
            [0, 1],
            [0.125, 0.9844],
            [0.25, 0.9394],
            [0.375, 0.8688],
            [0.5, 0.7788],
            [0.625, 0.6766],
            [0.75, 0.5697],
            [0.875, 0.465],
            [1, 0.3678]
        ]

        self.assertAlmostEqual(0.7458, trapezoid_integral_from_points(chosen_points), 4)

    def test_trapezoid_sin_integral_from_points2(self):
        chosen_points = [
        ]

        x0 = 0
        for i in range(11):
            chosen_points.append([x0+0.1*i, (x0+0.1*i)**4])

        self.assertAlmostEqual(0.2000, trapezoid_integral_from_points(chosen_points), 2)

    def test_trapezoid_sin_integral_from_points3(self):
        chosen_points = [
        ]

        x0 = 0
        for i in range(11):
            chosen_points.append([x0+0.1*i, (x0+0.1*i)**5])

        self.assertAlmostEqual(0.1667, trapezoid_integral_from_points(chosen_points), 2)

