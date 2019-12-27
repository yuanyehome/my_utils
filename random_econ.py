from math import *
from my_functions import *


class rand_calc:
    def __init__(self, mu, var):
        self.mu = mu
        self.sigma = sqrt(var)

    def calc_a(self, n):
        '''
        计算随机利率终值
        '''
        return exp(n * self.mu + n * self.sigma ** 2 / 2), \
            sqrt(exp(2 * n * self.mu + n * self.sigma ** 2)
                 * (exp(n * self.sigma ** 2) - 1))

    def calc_a_iver(self, n):
        '''
        计算随机利率现值
        '''
        return exp(-n * self.mu + n * self.sigma ** 2 / 2), \
            sqrt(exp(-2 * n * self.mu + n *
                     self.sigma ** 2) * (exp(n * self.sigma ** 2) - 1))

    def calc_s(self, n):
        '''
        计算随机利率期末年金终值
        '''
        mean_n = 0
        var_n = 0
        for i in range(n):
            mean_n += self.calc_a(i)[0]
            var_n += self.calc_a(i)[1]
        return mean_n, sqrt(var_n)

    def calc_dot_s(self, n):
        '''
        计算随机利率期初年金终值
        '''
        mean_n = 0
        var_n = 0
        for i in range(n):
            mean_n += self.calc_a(i + 1)[0]
            var_n += self.calc_a(i + 1)[1] ** 2
        # print(var_n)
        # for i in range(n):
        #     j = i + 1
        #     while j < n:
        #         var_n += (self.calc_a(2)[0] ** (i + 1)) * (self.calc_a(1)[0] ** (j - i)) \
        #             - self.calc_a(i + 1)[0] * self.calc_a(j + 1)[0]
        #         j += 1
        # print(var_n)
        return mean_n, sqrt(var_n)

    def calc_a_n(self, n):
        '''
        计算随机利率期末年金现值
        '''
        mean_n = 0
        var_n = 0
        for i in range(n):
            mean_n += self.calc_a_iver(i + 1)[0]
            var_n += self.calc_a_iver(i + 1)[1] ** 2
        return mean_n, sqrt(var_n)

    def calc_dot_a_n(self, n):
        '''
        计算随机利率期初年金现值
        '''
        mean_n = 0
        var_n = 0
        for i in range(n):
            mean_n += self.calc_a_iver(i)[0]
            var_n += self.calc_a_iver(i)[1] ** 2
        return mean_n, sqrt(var_n)


def calc_price(S, E, T):
    pass


if __name__ == "__main__":
    calculater = rand_calc(0.06, 0.01)
