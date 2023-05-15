import sys
input = sys.stdin.readline
import heapq

def dijkstra(graph, start):
    dis = {node: float('inf') for node in graph}
    dis[start] = 0
    q = []
    heapq.heappush(q,[dis[start],start])
    
    while q:
        nowDis, nowNode = heapq.heappop(q)
        
        if dis[nowNode] < nowDis:
            continue
        
        for newNode, newDis in graph[nowNode].items():
            tempDis = nowDis + newDis
            if tempDis < dis[newNode]:
                dis[newNode] = tempDis
                heapq.heappush(q,[tempDis,newNode])
    return dis

v,e = map(int,input().split())
start = int(input())
graph = {i:{} for i in range(1,v+1)}
for _ in range(e):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v],w)
    else:
        graph[u][v] = w

ansDict = dijkstra(graph,start)
for i in ansDict.values():
    if i == float('inf'):
        print('INF')
    else:
        print(i)
        