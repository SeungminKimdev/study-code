import sys
input = sys.stdin.readline

def remote(target, m, broke):
    now = 100
    ans = abs(target - now)
    if m == 0 or target == 100:
        return print(min(ans,len(str(target))))
    
    maxNum = int('9' * (len(str(target)) + 1))
    for i in range(maxNum):
        check = True
        for j in str(i):
            if int(j) in broke:
                check = False
                break
        if check:
            ans = min(ans,len(str(i)) + abs(target - i))
    return print(ans)

N = int(input())
M = int(input())
broken = []
if M != 0:
    for i in input().split():
        broken.append(int(i))
remote(N,M,broken)