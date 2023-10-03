import sys
input = sys.stdin.readline
import heapq
INF = 99999999

class Party:
    def __init__(self, N, M, X):
        self.n = N
        self.m = M
        self.x = X-1
        self.distance = []
        self.distanceR = []
        for i in range(self.n):
            self.distance.append([INF]*n)
            self.distanceR.append([INF]*n)
            self.distance[i][i] = 0
            self.distanceR[i][i] = 0
        for _ in range(self.m):
            start, end, tempDis = map(int,input().split())
            self.distance[start-1][end-1] = tempDis
            self.distanceR[end-1][start-1] = tempDis

    def dijkstra(self, tempDis):
        dis = [i for i in tempDis[self.x]]
        visited = [False] * self.n
        visited[self.x] = True
        hq = []
        for i in range(self.n):
            heapq.heappush(hq,(dis[i],i))
            
        while hq:
            nowDis,nowVill = heapq.heappop(hq)
            if visited[nowVill] or nowDis > dis[nowVill]:
                continue
            visited[nowVill] = True
            for i in range(self.n):
                if not visited[i] and nowDis + tempDis[nowVill][i] < dis[i]:
                    dis[i] = nowDis + tempDis[nowVill][i]
                    heapq.heappush(hq,(dis[i],i))
        return dis

if __name__ == '__main__':
    n, m, x = map(int,input().split())
    party = Party(n,m,x)
    dis1 = party.dijkstra(party.distance)
    dis2 = party.dijkstra(party.distanceR)
    answer = 0
    for i in range(n):
        answer = max(answer,dis1[i]+dis2[i])
    print(answer)