# Let's compute APSP of the graph.  Then, since n <= 5 we can go over all possible permutations of
# ways we can go to visit the bunnies and use the APSP table to find the distance to visit each bunny 
#
# We use floyd warshall to check for negative cycles.  If there is a negative cycle, than we can definitely
# save everyone

from itertools import permutations

def solution(times, times_limit):
    n = len(times)
    
    # convert adj matrix to distance array
    # also for checking negative cycle
    for _ in range(100): # maybe ?????
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    times[i][j] = min(times[i][j], times[i][k] + times[k][j])
    
    # check for negative cycle
    for i in range(n):
        if times[i][i] < 0:
            return range(n-2)
    
    # go over all permutation
    ans = []
    for p in permutations(range(1, n-1)):
        b_time = 0 # time to last bunny
        last_loc = 0
        for i in range(n-2):
            b_time += times[last_loc][p[i]]
            last_loc = p[i]
            
            tot_time = b_time + times[p[i]][n-1]
            if tot_time <= times_limit:
                cur_ans = list(p[:i+1])
                cur_ans.sort()
                if len(cur_ans) > len(ans):
                    ans = cur_ans
                elif len(cur_ans) == len(ans) and cur_ans < ans:
                    ans = cur_ans
    
    # we have node indices, change them to bunny indices
    for i in range(len(ans)):
        ans[i] -= 1
    
    return ans
