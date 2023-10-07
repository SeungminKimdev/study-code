import sys
input = sys.stdin.readline
INF = int(1e9)

class Wormhole:
    def __init__(self):
        self.n, self.m, self.w = map(int,input().split())
        self.road = []
        for _ in range(self.m): #도로(양방향)
            s,e,t = map(int,input().split())
            self.road.append((s-1,e-1,t))
            self.road.append((e-1,s-1,t))
        for _ in range(self.w): #웜홀(단방향 음수)
            s,e,t = map(int,input().split())
            self.road.append((s-1,e-1,-t))
    
    def bellmanford(self,start):
        dis = [INF] * self.n
        dis[start] = 0
        for i in range(self.n):
            for now,nextNode,cost in self.road:
                if dis[nextNode] > dis[now] + cost:
                    dis[nextNode] = dis[now] + cost
                    if i == self.n - 1:
                        return print('YES')
        return print('NO')

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        wormhole = Wormhole()
        wormhole.bellmanford(0)