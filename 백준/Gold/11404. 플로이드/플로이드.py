import sys
input = sys.stdin.readline
INF = 99999999

def solution():
    n = int(input())
    m = int(input())
    cost = {}
    for i in range(n):
        cost[i] = [INF for _ in range(n)]
        cost[i][i] = 0
    
    for _ in range(m):
        a,b,c = map(int,input().split())
        cost[a-1][b-1] = min(cost[a-1][b-1], c)
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j],cost[i][k] + cost[k][j])

    for i in range(n):
        ans = ''
        for j in cost[i]:
            if j == INF:
                ans += '0 '
            else:
                ans += str(j)
                ans += ' '
        print(ans.rstrip())

if __name__ == '__main__':
    solution()