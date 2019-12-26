from my_functions import solve, calc_a
from math import floor


def func(left_years, r, p):
    d = floor(left_years)
    f = left_years - floor(left_years)
    return lambda x: (1 + x)**f * p - 100 / ((1 + x)**d) - 100 * r * (1 + calc_a(d, x))


print(solve(0, 1, func(4.7836, 0.0295, 96.355)))
print(solve(0, 1, func(1.6219, 0.0329, 103.932)))
print(solve(0, 1, func(27.9836, 0.0327, 85.245)))
