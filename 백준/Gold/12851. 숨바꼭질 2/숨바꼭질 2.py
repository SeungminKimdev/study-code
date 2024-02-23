import sys
input = sys.stdin.readline
from collections import deque
q = deque()
visited = [False] * 200001
n,k = map(int,input().split())
visited[n] = True
ansT = 0
ans = 1
q.append((n,0))

while q:
    now,nowT = q.popleft()
    if now == k:
        ansT = nowT
        print(nowT)
        break
    visited[now] = True

    if now < k:
        if not visited[now*2]:
            q.append((now*2,nowT+1))
        if not visited[now+1]:
            q.append((now+1,nowT+1))
    if now > 0:
        if not visited[now-1]:
            q.append((now-1,nowT+1))

while q:
    now,nowT = q.popleft()
    if now == k and nowT == ansT:
        ans += 1
print(ans)