import sys
import heapq
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
    
    visited = [False] * n
    mst = []
    min_heap = [(0, 0)]
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst.append(weight)
        
        for next_node, next_weight in graph[u]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_weight, next_node))
    
    print(sum(mst) - max(mst))


if __name__ == "__main__":
	main()