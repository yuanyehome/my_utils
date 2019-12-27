from math import *
import my_functions
import scipy.stats


def get_prob(x):
    return scipy.stats.norm(0, 1).cdf(x)


class rand_calc:
    def __init__(self, mu, var):
        self.mu = mu
        self.sigma = sqrt(var)

    def calc_ij(self):
        self.i = self.calc_a(1)[0] - 1
        self.j = 2 * self.i + self.i ** 2 + self.calc_a(1)[1] ** 2
        self.i_iver = 1 / self.calc_a_iver(1)[0] - 1
        self.k_iver = 1 / exp(-2 * self.mu + 4 * self.sigma ** 2 / 2) - 1

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
        tmp = self.calc_dot_s(n - 1)
        return tmp[0] + 1, tmp[1]

    def calc_dot_s(self, n):
        '''
        计算随机利率期初年金终值
        '''
        mean_n = 0
        var_n = 0
        for i in range(n):
            mean_n += self.calc_a(i + 1)[0]
        m1 = 1 + self.i
        m2 = 1 + self.j
        sj = my_functions.calc_dot_s(n, self.j)
        si = my_functions.calc_dot_s(n, self.i)
        var_n = (m2 + m1) / (m2 - m1) * sj - 2 * m2 / (m2 - m1) * si - si ** 2
        return mean_n, sqrt(var_n)

    def calc_a_n(self, n):
        '''
        计算随机利率期末年金现值
        '''
        mean_n = 0
        var_n = 0
        for i in range(n):
            mean_n += self.calc_a_iver(i + 1)[0]
        ai = my_functions.calc_a(n, self.i_iver)
        ak = my_functions.calc_a(n, self.k_iver)
        m1 = 1 / (1 + self.i_iver)
        m2 = 1 / (1 + self.k_iver)
        var_n = (m2 + m1) / (m2 - m1) * ak - 2 * m2 / (m2 - m1) * ai - ai ** 2
        return mean_n, sqrt(var_n)

    def calc_dot_a_n(self, n):
        '''
        计算随机利率期初年金现值
        '''
        tmp = self.calc_a_n(n - 1)
        return tmp[0] + 1, tmp[1]


def calc_price(S, E, T, delta, std):
    d1 = (log(S / E) + (delta + 1 / 2 * std ** 2) * T) / (std * sqrt(T))
    d2 = (log(S / E) + (delta - 1 / 2 * std ** 2) * T) / (std * sqrt(T))
    C = S * get_prob(d1) - exp(-delta * T) * E * get_prob(d2)
    P = exp(-delta * T) * E * get_prob(-d2) - S * get_prob(-d1)
    return C, P


if __name__ == "__main__":
    print(calc_price(0.00001, 1, 1, 0.1, 0.3))
