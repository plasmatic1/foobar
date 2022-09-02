# Consider what happens when the beam hits a corner or a wall: it bounces off the wall in the opposite
# direction, flipping the X and/or Y velocity.  Now consider flipping the entire room instead of 
# just the beam itself- this has the same effect.  If we then stack this flipped room on top of the 
# room that the beam just hit the wall of, then we can picture the beam going into the stacked room
# instead of staying in the original copy of the room.  This has the added benefit of letting us
# easily compute the distance from the start to the target.
#
# Now, let's extend these clones of the room infinitely in the X and Y directions, and number each 
# clone with a coordinate.  Each clone has a copy of the target, and reaching each cloned target 
# directly represents a way to reach the original target with some number of bounces.  Thus, we only
# need to compute the direction we're travelling in to each cloned target within max_dist of the 
# starting point.  We can do this by just finding a loose upper bound for the max coordinate of
# a clone (approx. (max_dist / width, max_dist / height)) and just brute-forcing all clones within
# that range.
#
# Note: make sure to also consider going from the starting point to itself.  If that is possible
# before reaching the goal, then don't count it

from collections import deque
from fractions import Fraction

def dist_sq(c1, c2):
    dx = abs(c1[0] - c2[0])
    dy = abs(c1[1] - c2[1])
    return dx**2 + dy**2
    
def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

infd = 10**9 # "infinity" distance

# same as the original problem except we ignore the fact that you can hit yourself
def get_slopes(dim, you, goal, max_dist):
    max_dist_sq = max_dist ** 2
    
    # compute coordinate of goal when given the coordinates for a clone of the original room
    # [0, 0] is the original room
    def get_goal_pos(grid_num):
        cur_goal = [goal[0], goal[1]]
        if grid_num[0] % 2: # flip x
            cur_goal[0] = dim[0] - cur_goal[0]
        if grid_num[1] % 2: # flip y
            cur_goal[1] = dim[1] - cur_goal[1]
        cur_goal[0] += grid_num[0] * dim[0] # add offset x
        cur_goal[1] += grid_num[1] * dim[1] # add offset y
        return cur_goal
    
    # KEY: (sgn, s_x, s_y) - sgn = whether coordinate is positive or negative (or zero), s_x, s_y = slope
    # VALUE: min dist to get to the goal in that direction
    slopes = {}
    max_cnt_x = (max_dist + dim[0] - 1) / dim[0]
    max_cnt_y = (max_dist + dim[1] - 1) / dim[1]
    for i in xrange(-max_cnt_x, max_cnt_x+1):
        for j in xrange(-max_cnt_y, max_cnt_y+1):
            grid_num = [i, j]
        
            # get goal coordinate of clone and calculate direction tuple
            cur_goal = get_goal_pos(grid_num)
            delta = [cur_goal[0] - you[0], cur_goal[1] - you[1]]
            if delta[0]**2 + delta[1]**2 > max_dist_sq: # break if too large
                continue
            
            if delta[0] == 0: # vertical slope
                key = (sign(delta[0]), sign(delta[1]), 0)
            else:
                f = Fraction(delta[1], delta[0])
                key = ((sign(delta[0]), f.numerator, f.denominator))
        
            # add distance to slopes
            dist = dist_sq(you, cur_goal)
            slopes[key] = min(slopes.get(key, infd), dist)
    
    return slopes
    
def solution(dim, you, goal, max_dist):
    slopes_goal = get_slopes(dim, you, goal, max_dist)
    slopes_you = get_slopes(dim, you, you, max_dist)
    
    ans = 0 # eliminate cases where you hit yourself first
    for key, dist in slopes_goal.items():
        if slopes_you.get(key, infd) > dist:
            ans += 1
    return ans
