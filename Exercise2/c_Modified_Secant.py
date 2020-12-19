def modified_secant(function, point_one, point_two, point_three, digits_of_precision):
    iteration_counter = 0

    f = function

    x1 = point_one
    x2 = point_two
    x3 = point_three

    while True:
        if f(x3) == 0:
            return x3, iteration_counter
        else:
            iteration_counter += 1

            q = f(x1) / f(x2)
            r = f(x3) / f(x2)
            s = f(x3) / f(x1)

            x_next = x3 - ( r * (r - q) * (x3 - x2) + (1 - r) * s * (x3 - x1) ) / ( (q - 1) * (r - 1) * (s - 1) )

            if abs(x_next - x3) < 0.5 * 10 ** (-1.0 * digits_of_precision):
                return x_next, iteration_counter
            else:
                x1 = x2
                x2 = x3
                x3 = x_next