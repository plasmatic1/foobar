nums = []
tot_len = 0

i = 2
while tot_len <= 10010:
    isp = True
    j = 2
    while j * j <= i:
        if i % j == 0:
            isp = False
            break
        j += 1
    
    if isp:
        nums.append(str(i))
        tot_len += len(str(i))

    i += 1

nums_str = ''.join(nums)

def solution(i):
    return nums_str[i:i+5]
    
