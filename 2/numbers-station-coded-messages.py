def solution(l, t):
    for i in range(len(l)):
        for j in range(i+1, len(l)+1):
            if sum(l[i:j]) == t:
                return [i, j-1]

    return [-1, -1]

