import sys
from collections import deque
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    indegree = [0] * (N + 1) # 들어오는 노드 수
    graph = [[] for _ in range(N + 1)] # 연결된 그래프 정보
    for _ in range(M):
        order = list(map(int, input().split()))
        for i in range(1, order[0]):
            graph[order[i]].append(order[i+1])
            indegree[order[i+1]] += 1
    
    answer = []
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        answer.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    if len(answer) != N:
        print(0)
    else:
        print(*answer, sep='\n')

if __name__ == "__main__":
    main()