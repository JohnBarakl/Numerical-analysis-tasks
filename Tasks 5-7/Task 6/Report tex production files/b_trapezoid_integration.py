from math import sin, pi


def trapezoid_integral_from_points(points):
    func_sum = 0

    a = points[0][0]
    b = points[len(points) - 1][0]
    N = len(points) - 1

    func_sum += points[0][1]
    func_sum += points[len(points) - 1][1]

    temp_sum = 0
    for i in range(1, len(points) - 1):
        temp_sum += points[i][1]

    func_sum += 2 * temp_sum

    integral = ((b - a) / (2 * N)) * func_sum

    return integral


def main():
    chosen_points = [
        [0, sin(0)],
        [pi / 20, sin(pi / 20)],
        [pi / 10, sin(pi / 10)],
        [pi * 3 / 20, sin(pi * 3 / 20)],
        [pi / 5, sin(pi / 5)],
        [pi / 4, sin(pi / 4)],
        [pi * 3 / 10, sin(pi * 3 / 10)],
        [pi * 7 / 20, sin(pi * 7 / 20)],
        [pi * 2 / 5, sin(pi * 2 / 5)],
        [pi * 9 / 20, sin(pi * 9 / 20)],
        [pi / 2, sin(pi / 2)]
    ]

    a = chosen_points[0][0]
    b = chosen_points[len(chosen_points) - 1][0]
    N = len(chosen_points) - 1

    sin_integral = trapezoid_integral_from_points(chosen_points)
    sin_integral_theoretical_error = (((b - a) ** 3) / (12 * N ** 2))
    arithmetical_error = sin_integral - 1

    print("Sin integral in [0, pi/2] with trapezoid from 11 chosen points: {:f}".format(sin_integral))
    print("Theoretical error: {:e}, and arithmetical error: {:e}".format(sin_integral_theoretical_error, arithmetical_error))


if __name__ == '__main__':
    main()
