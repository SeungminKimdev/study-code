import sys
input = sys.stdin.readline
import math
import heapq

def makeDis(point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def prim(points):
    n = len(points)
    visited = [False] * n
    mst = []
    disMat = [[makeDis(points[i],points[j]) for j in range(n)] for i in range(n)]
    pq = [(0,0)]
    while len(mst) < n:
        dis,nowPoint = heapq.heappop(pq)
        if visited[nowPoint]:
            continue
        visited[nowPoint] = True
        mst.append((nowPoint,dis))
        for nextPoint,nextDis in enumerate(disMat[nowPoint]):
            if not visited[nextPoint]:
                heapq.heappush(pq,(nextDis,nextPoint))
    return mst

if __name__ == '__main__':
    n = int(input())
    points = [tuple(map(float,input().split())) for _ in range(n)]
    mst = prim(points)
    total = sum(dis for _,dis in mst)
    print(round(total,2))