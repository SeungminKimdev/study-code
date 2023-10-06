import sys
input = sys.stdin.readline
from collections import deque

def solution():
    n, k = map(int,input().split())
    location = deque([n])
    visited = [0] * 100001
    visited[n] = 1
    while location:
        now = location.popleft()
        if now == k:
            return visited[now] - 1
        if now * 2 < 100001 and visited[now*2] == 0:
            location.appendleft(now*2)
            visited[now*2] = visited[now]
        if now - 1 >= 0 and visited[now-1] == 0:
            location.append(now-1)
            visited[now-1] = visited[now] + 1
        if now + 1 < 100001 and visited[now+1] == 0:
            location.append(now+1)
            visited[now+1] = visited[now] + 1

if __name__ == '__main__':
    print(solution())