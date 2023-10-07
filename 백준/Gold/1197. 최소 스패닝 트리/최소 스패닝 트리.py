import sys
input = sys.stdin.readline
import heapq

class Mst:
    def __init__(self):
        self.v, self.e = map(int,input().split())
        self.loot = {i:[] for i in range(self.v)}
        for _ in range(self.e):
            a,b,c = map(int,input().split())
            self.loot[a-1].append((c,b-1))
            self.loot[b-1].append((c,a-1))
    
    def primMst(self,start):
        visited = [False] * self.v
        hq = [(0,start)]
        ans = 0
        while hq:
            cost, nextNode = heapq.heappop(hq)
            if not visited[nextNode]:
                ans += cost
                for i in self.loot[nextNode]:
                    heapq.heappush(hq,i)
                visited[nextNode] = True
        return print(ans)

if __name__ == '__main__':
    mst = Mst()
    mst.primMst(0)