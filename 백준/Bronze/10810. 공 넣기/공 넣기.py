import sys
input = sys.stdin.readline

n, m = map(int,input().split())
pocket = [[0] for _ in range(n)]
for _ in range(m):
    i,j,k = map(int,input().split())
    for i1 in range(i-1,j):
        pocket[i1].append(k)
        
answer = ""
for i in range(n):
    answer += str(pocket[i][-1])
    answer += " "
print(answer)