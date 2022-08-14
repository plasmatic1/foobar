# Obs. 0: Gear ratios:
#   - for gears with radii a_1, a_2, gear 2 will spin at a_1/a_2 speed assuming gear 1 is spinning at unit speed
# Obs. 1: Fixing gear 1 will fix the radii and thus spin speed of all other gears
# Obs. 2: Only the radii of the first and last gear matter

# Eqn of the form: c - m * r, where c = some real, m = +-1, r = radius of gear 1
#   Initially: c = 0, m = -1
#   When adding a new gear, the eqn becomes:
#     c_0 - (c - m * r)
#     c_0 - c + m * r
#     (c_0 - c) - (-m) * r
#   So:
#     c := c_0 - c
#     m := -m
#   Noting that c_0 = gap between pegs
#
#   At the end, we must find some r s.t.
#     r / (c - m * r) = 2
#     r = 2 * c - 2 * m * r
#     (1 + 2 * m) * r = 2 * c
#     r = (2 * c) / (2 * m + 1)

# Note: at each point, we must make sure the gear used has radius >= 1

from fractions import Fraction

def solution(pegs):
    c = 0
    m = -1
    for i in range(len(pegs)-1):
        c_0 = pegs[i+1] - pegs[i]
        c = c_0 - c
        m = -m
    
    r = Fraction(2 * c, 2 * m + 1)

    # check that the solution is valid (r is non-negative)
    if r < 1:
        return [-1, -1]
    
    # check that the solution is valid (no gears go out of bounds)
    cur_r = r
    for i in range(len(pegs)-1):
        c_0 = pegs[i+1] - pegs[i]
        cur_r = c_0 - cur_r
        if cur_r < 1:
            return [-1, -1]
    
    # return answer otherwise
    return [r.numerator, r.denominator]
