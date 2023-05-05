import sys
input = sys.stdin.readline

def ans(n,stairs):
    if n == 1:
        return stairs[0]
    elif n == 2:
        return stairs[0] + stairs[1]
    
    score = [0 for _ in range(n)]
    score[0] = stairs[0]
    score[1] = max(stairs[1],stairs[0] + stairs[1])
    score[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])
    for i in range(3,n):
        score[i] = stairs[i] + max(score[i-2], stairs[i-1]+score[i-3])
    return score[n-1]

N = int(input())
stairs = [int(input()) for _ in range(N)]
print(ans(N,stairs))