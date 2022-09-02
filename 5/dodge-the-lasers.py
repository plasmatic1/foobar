# Overall problem: sum_{i=1..n} floor(sqrt(2) * i)
#
# we can compute very accurate approximations of sqrt(2) using continued fractions
# * Compute the value using approximation and flooring.  Just make sure the approximation is larger than sqrt(2)
# * Could always use fractions.Fraction() to store the result
# * Reduces to sum{i=1..n} floor(i * p/q) where p,q are coprime
#   * From: https://open.kattis.com/problems/itsamodmodmodmodworld

import math
from fractions import Fraction

# From: https://open.kattis.com/problems/itsamodmodmodmodworld
# Computes sum{i=1..n} floor(a*i/m)
def sum_floor_linear(n, m, a):
    if n == 0:
        return 0

    ans = 0;
    if a >= m:
        ans += (a // m) * (n * (n + 1) // 2)
        a %= m

    if a == 0:
        return ans

    n0 = (n * a) // m # max
    m0 = a
    a0 = m

    ans += n0 * n
    ans -= sum_floor_linear(n0, m0, a0)
    ans += n0 // a

    return ans

def solution(n):
    n = int(n) # convert
    
    sqrt_2 = Fraction(1, 1)
    for _ in range(300):
        sqrt_2 = 2 + 1 / sqrt_2
    sqrt_2 = 1 + 1 / sqrt_2

    assert sqrt_2**2 > 2  # Make sure we have an upper approximation

    ans = sum_floor_linear(n, sqrt_2.denominator, sqrt_2.numerator)
    return str(ans) # convert

