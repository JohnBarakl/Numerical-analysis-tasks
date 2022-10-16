def modified_newton_raphson(function, function_derivative, function_second_derivative, starting_point, digits_of_precision):
    iteration_counter = 0

    f = function
    f_d = function_derivative
    f_dd = function_second_derivative

    x = starting_point

    while True:
        if f(x) == 0:
            return x, iteration_counter
        else:
            iteration_counter += 1
            x_next = x - (f(x) / f_d(x)) - (1/2) * ( (f(x) ** 2 * f_dd(x)) / (f_d(x)**3) )

            if abs(x_next - x) < 0.5 * 10 ** (-1.0 * digits_of_precision):
                return x_next, iteration_counter
            else:
                x = x_next