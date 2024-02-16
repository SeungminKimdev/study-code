import sys
input = sys.stdin.readline
import heapq

class Graph:
    def __init__(self,N,E):
        self.n = N
        self.e = E
        self.gp = [[1e8]*(N) for _ in range(N)]
        for i in range(N):
            self.gp[i][i] = 0
        for _ in range(E):
            a, b, c = map(int,input().split())
            self.gp[a-1][b-1] = c
            self.gp[b-1][a-1] = c
        self.target1, self.target2 = map(int,input().split())
        self.target1 -= 1
        self.target2 -= 1

    def dijkstra(self,start):
        tempDist = [0] * self.n
        visited = [False] * self.n
        for i in range(self.n):
            tempDist[i] = self.gp[start][i]
        visited[start] = True
        hq = []
        for i in range(self.n-2):
            for t in range(self.n):
                if not visited[t]:
                    heapq.heappush(hq,(tempDist[t],t))
            now = heapq.heappop(hq)[1]
            hq = []
            visited[now] = True
            for j in range(self.n):
                if not visited[j]:
                    if tempDist[now] + self.gp[now][j] < tempDist[j]:
                        tempDist[j] = tempDist[now] + self.gp[now][j]
        return tempDist

    def makeAns(self):
        dk1 = self.dijkstra(self.target1)
        dk2 = self.dijkstra(self.target2)
        ans1 = dk1[0] + dk1[self.target2] + dk2[self.n-1]
        ans2 = dk2[0] + dk2[self.target1] + dk1[self.n-1]
        answer = min(ans1,ans2)
        if answer >= 1e8:
            answer = -1
        return print(answer)

N,E = map(int,input().split())
graph = Graph(N,E)
graph.makeAns()