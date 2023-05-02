import sys
input = sys.stdin.readline

N, M = map(int, input().split())
relation = [[101 for _ in range(N)] for _ in range(N)]

for i in range(N):
    relation[i][i] = 0
    
for _ in range(M):
    a, b = map(int, input().split())
    relation[a-1][b-1] = 1
    relation[b-1][a-1] = 1
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            relation[i][j] = min(relation[i][j],relation[i][k] + relation[k][j])
            
ans = []
for i in relation:
    ans.append(sum(i))
    
print(ans.index(min(ans)) + 1)