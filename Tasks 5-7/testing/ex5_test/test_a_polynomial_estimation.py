from unittest import TestCase

from Exercise5.a_polynomial_approximation import polynomial_approximate


class Test(TestCase):
    def test_polynomial_approximate1(self):
        self.assertEqual(polynomial_approximate(
            [
                [-2, -9],
                [-1, -2],
                [0, -1],
                [1, 0]
            ]
        ), [-1, 0, 0, 1])

    def test_polynomial_approximate2(self):
        self.assertEqual(polynomial_approximate(
            [
                [-1, 20],
                [0, 10],
                [2, -4]
            ]
        ), [10, -9, 1])

    def test_polynomial_approximate3(self):
        self.assertEqual(polynomial_approximate(
            [
                [0, -3],
                [5, 7]
            ]
        ), [-3, 2])

    def test_polynomial_approximate3(self):
        self.assertEqual(polynomial_approximate(
            [
                [0, 2],
                [1, 1],
                [2, 0],
                [3, -1]
            ]
        ), [2, -1, 0, 0])

    def test_polynomial_approximate4(self):
        c = 0
        res = [1, -0.5, 0.5]
        for i in polynomial_approximate(
                [
                    [0, 1],
                    [2, 2],
                    [3, 4]
                ]):
            self.assertAlmostEqual(i, res[c])
            c += 1
