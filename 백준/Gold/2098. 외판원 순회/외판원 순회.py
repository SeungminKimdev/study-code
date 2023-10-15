import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
INF = int(1e9)

class Tsp:
    def __init__(self,n):
        self.n = n
        self.road = []
        for _ in range(n):
            self.road.append(list(map(int,input().split())))
        self.memo = {}
        self.maxBit = (1<<self.n) - 1
        
    def tsp(self, now, visited):
        if visited == self.maxBit:
            if self.road[now][0]:
                return self.road[now][0]
            else:
                return INF
        
        if (now,visited) in self.memo:
            return self.memo[(now,visited)]
        
        minDis = INF
        for i in range(1,self.n):
            if visited & (1<<i) or self.road[now][i] == 0:
                continue
            dis = self.road[now][i] + self.tsp(i,visited | (1<<i))
            minDis = min(minDis,dis)
        
        self.memo[(now,visited)] = minDis
        return minDis

if __name__ == '__main__':
    n = int(input())
    tspC = Tsp(n)
    print(tspC.tsp(0,1))