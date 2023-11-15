import sys
input = sys.stdin.readline

request = list(map(int,input().split()))
request.pop()
length = len(request)
if length == 0:
    print(0)
    exit()
dp = [[[999999]*5 for _ in range(5)] for _ in range(length+1)]
dp[-1][0][0] = 0

def move(a, b):
    if a == 0:
        if b == 0:
            return 0
        else:
            return 2
    elif a == b:
        return 1
    elif abs(b-a) == 1 or abs(b-a) == 3:
        return 3
    else:
        return 4

for i in range(length):
    for r in range(5):
        for k in range(5):
            moveL = move(k,request[i])
            dp[i][request[i]][r] = min(dp[i][request[i]][r],dp[i-1][k][r] + moveL)
        
    for l in range(5):
        for k in range(5):
            moveR = move(k,request[i])
            dp[i][l][request[i]] = min(dp[i][l][request[i]],dp[i-1][l][k] + moveR)
            
ans = int(1e9)
for l in range(5):
    for r in range(5):
        ans = min(ans,dp[length-1][l][r])
print(ans)