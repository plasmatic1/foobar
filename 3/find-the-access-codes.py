# Essentially, run DP but the DP state is being updated in a rolling manner (like O(W) memory 0-1 knapsack)
# dp[i][j] := dict where dict[x] is the number of j-tuples ending at index <= i

from collections import Counter

def solution(l):
    count = [Counter() for _ in range(3)]
    tot = 0

    for x in l:
        # get factors
        factors = []
        f = 1
        while f * f <= x:
            if x % f == 0:
                factors.append(f)
                if f * f != x: factors.append(x / f)
            f += 1
        factors.sort(reverse=True)

        # update count with new value
        for f in factors:
            if f in count[1]:
                count[2][x] += count[1][f]
            if f in count[0]:
                count[1][x] += count[0][f]
        count[0][x] += 1 # initial value

    return sum(count[2].values())
