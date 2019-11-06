from math import *


def calc_a(n_, i_):
    '''计算标准期末年金现值；'''
    v = 1 / (1 + i_)
    return (1 - v ** n_) / i_


def calc_s(n_, i_):
    '''计算标准期末年金终值'''
    return calc_a(n_, i_) * ((1 + i_) ** n_)


def calc_dot_a(n_, i_):
    '''计算标准期初年金现值'''
    return (1+i_) * calc_a(n_, i_)


def calc_dot_s(n_, i_):
    '''计算标准期初年金终值'''
    return calc_dot_a(n_, i_) * ((1 + i_) ** n_)


def calc_Ia(n_, i_):
    '''计算标准递增期末年金现值'''
    return (calc_dot_a(n_, i_) - n_ * ((1 / (1 + i_) ** n_))) / i_


def calc_Is(n_, i_):
    '''计算标准递增期末年金终值'''
    return (calc_dot_a(n_, i_) - n_ * ((1 / (1 + i_) ** n_))) / i_ * ((1 + i_) ** n_)


def calc_Da(n_, i_):
    '''计算标准递减期末年金现值'''
    return (n_ - calc_a(n_, i_)) / i_


def calc_Ds(n_, i_):
    '''计算标准递减期末年金终值'''
    return (n_ - calc_a(n_, i_)) / i_ * ((1 + i_) ** n_)


def calc_p_q(p_, q_, n_, i_):
    '''计算等量变化年金现值'''
    return (p_ - q_) * calc_a(n_, i_) + q_ * calc_Ia(n_, i_)


def solve(a, b, func, eps=1e-5):
    '''二分法求解函数零点，a->min, b->max, eps默认1e-5'''
    while (b - a >= eps):
        tmp = (a + b) / 2
        if (func(tmp) > 0):
            b = tmp
        elif (func(tmp) < 0):
            a = tmp
        else:
            return tmp
    return a


def Solver(n, i, j):
    '''求解4.2.4式，求解偿债基金利率和贷款利率综合下的实际还贷利率'''
    c = calc_a(n, j) / (1 + (i - j) * calc_a(n, j))
    a_ = 0
    b_ = c

    def func_(r):
        return c * r + (1 / (1 + r)) ** n - 1
    ans = solve(a_, b_, func_)
    return ans
