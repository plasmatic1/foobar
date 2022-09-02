# Let v_0 = [1, 0, ...]
# Let A be the transition matrix
#
# Let A' = I + A + A^2 + A^3 + ... = a/(1-r) = I/(I-A) = (I-A)^-1
# Notice that if we can compute A', then this gives us the long run behaviour of 
# the system given a starting state.  In this case, computing v' = A'v_0 gives us
# the vector that we want.  Just make sure to only isolate the states that are terminal

from fractions import Fraction

def get_gcd(a, b):
    return a if b == 0 else get_gcd(b, a % b)

def get_lcm(nums):
    lcm = 1
    for x in nums:
        lcm = lcm * x / get_gcd(lcm, x)
    return lcm

# from, to, alpha
def v_add(f, t, a):
    for i in range(len(f)):
        t[i] += f[i] * a

# to, alpha
def v_scale(t, a):
    for i in range(len(t)):
        t[i] *= a

# gaussian elim
def gaussian(mat):
    n = len(mat)
    m = len(mat[0])
    
    for i in range(n):
        # find pivot
        p_col = -1
        sw_row = -1
        for j in range(m):
            for k in range(i, n):
                if mat[k][j] != 0:
                    p_col = j
                    sw_row = k
                    break
            
            if p_col != -1:
                break
        
        # if no pivot, exit
        if p_col == -1:
            return
        
        # else, swap up to the top row, and subtract all the other rows
        mat[i], mat[sw_row] = mat[sw_row], mat[i]
        v_scale(mat[i], Fraction(1, mat[i][p_col]))
        for j in range(0, n):
            if j != i:
                v_add(mat[i], mat[j], -mat[j][p_col])

def solution(m):
    n = len(m)
    terminal = []
    for i, row in enumerate(m):
        tot = sum(row)
        
        # check terminal state
        if tot == 0:
            terminal.append(i)

        # change values into probabilities
        for j in range(n):
            if tot != 0:
                m[i][j] = Fraction(m[i][j], tot)
            else:
                m[i][j] = Fraction(0, 1)
    
    # transpose matrix
    m = list(zip(*m))
    for i in range(n): # convert back to list
        m[i] = list(m[i])
    
    # compute (I-A)^-1
    for i in range(n): # A -> I-A
        for j in range(n):
            m[i][j] *= -1
            if i == j:
                m[i][j] += 1

    for i in range(n): # augment with I
        id_row = [1 if j == i else 0 for j in range(n)]
        m[i].extend(id_row)
    
    gaussian(m) # do gaussian elim
    for i in range(n):
        m[i] = m[i][n:]
        
    ans_fracs = [] # implicitly get wanted values of A'v_0
    for x in terminal:
        ans_fracs.append(m[x][0])
    
    # format result
    lcm = get_lcm([f.denominator for f in ans_fracs])
    result = [f.numerator * (lcm / f.denominator) for f in ans_fracs]
    result.append(lcm)
    
    return result
