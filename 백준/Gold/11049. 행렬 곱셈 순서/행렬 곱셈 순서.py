import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dp = [[0] * n for _ in range(n)]
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

for term in range(1,n): #행렬 간격
    for start in range(n): #시작 부분
        end = start + term
        if end == n:
            break
        dp[start][end] = INF
        for t in range(start,end):
            dp[start][end] = min(dp[start][end],
                                dp[start][t] + dp[t+1][end]+(
                                    array[start][0]*array[t][1]*array[end][1]
                                ))

print(dp[0][n-1])