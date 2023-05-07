import sys
input = sys.stdin.readline

def findBro(n: int, m: int) -> int:
    timeLine = [-1] * (max(n,m)*2+1)
    q = [n]
    now = n
    timeLine[now] = 0
    while timeLine[m] == -1:
        now = q.pop(0)
        if timeLine[now+1] == -1:
            q.append(now+1)
            timeLine[now+1] = timeLine[now] + 1
        if now < m:
            if timeLine[now*2] == -1:
                q.append(now*2)
                timeLine[now*2] = timeLine[now] + 1
        if now > 0:
            if timeLine[now-1] == -1:
                q.append(now-1)
                timeLine[now-1] = timeLine[now] + 1
    return timeLine[m]

n, m = map(int,input().split())
print(findBro(n,m))