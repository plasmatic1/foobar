# Test brute force algorithm
#
# Idea: complimentary counting - get floor(sqrt(2) * (1+2+3+...+n)) and count the difference
# between that and the answer
#
# Can we compute the difference?
# ---------------------------------------------
# Let f(x) = floor(sum(i=1..n, i*sqrt(2)))
#     g(x) = sum(i=1..n, floor(i*sqrt(2)))
# ---------------------------------------------
# Note 1: Let's start by looking at the difference f(x)-g(x) over time
#       - Clearly, f(x) >= g(x)
#       - It increases at an approximately linear rate, around 1 for every 2 numbers
#       - Tracking when it changes in value, it's approximately even
# ---------------------------------------------
# Note 2: Let d(x) = f(x) - g(x).  Look at d(x) over time
#       - d(x) ~= x/2
#       - Could d(x) = floor(x/2) ?
#         - Error due to precision issues
# ---------------------------------------------

from fractions import Fraction

# sqrt_2 = Fraction(1)
# for _ in range(1000):
#     sqrt_2 = 2 + 1 / sqrt_2
# sqrt_2 = 1 + 1 / sqrt_2

from math import *

sqrt_2 = sqrt(2)

tsum = 0
fsum = 0

for i in range(1, 10000):
    tsum += sqrt_2 * i
    fsum += int(sqrt_2 * i)

    ttsum = int(tsum)
    d = tsum - fsum

    tsum_v = int(ttsum)
    fsum_v = int(fsum)
    approximate_v = int(tsum-i//2)
    ok = fsum_v == approximate_v
    print(i, tsum_v, fsum_v, approximate_v, d/i)
    # if not ok:
    #     print(i, float(d/i), ok)
