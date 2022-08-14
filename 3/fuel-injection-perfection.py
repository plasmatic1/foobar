# Defn: n is 'oddish' if n % 2 == 0 but n % 4 != 0
# General notes:
#   If n is even, definitely n := n // 2
#   If n is odd, usually you want to do n := n - 1, but sometimes it's advantageous to do n := n + 1 (i.e. n=15)
#     This is when we can do n := n // 2 multiple times (AKA n is not oddish)

# Obs 1: either n-1 or n+1 (and only one of them) is oddish
#   Greedy soln: if n is odd, take whichever one is not oddish
#     Exception: n=3 (you can't divide by 2 multiple times)

def solution(n):
    steps = 0
    n = int(n)
    
    while n > 1:
        if n % 2 == 0:
            n >>= 1
        else:
            if (n + 1) % 4 == 0 and n > 3:
                n += 1
            else:
                n -= 1
        
        steps += 1
    
    return steps
