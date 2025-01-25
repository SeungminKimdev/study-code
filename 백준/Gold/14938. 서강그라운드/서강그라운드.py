import sys
input = sys.stdin.readline
INF = int(1e9)

def floyd_warshall(n, graph):
    for k in range(n): # 중간 노드
        for a in range(n):
            for b in range(n):
                if a == b:
                    graph[a][b] = 0
                else:
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph

def main():
    n, m, r = map(int, input().split())
    items = list(map(int, input().split()))
    loads = [[INF] * n for _ in range(n)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        loads[a-1][b-1] = l
        loads[b-1][a-1] = l
    
    loads = floyd_warshall(n, loads)
    
    answer = 0
    for start in range(n):
        sum_scores = 0
        for end in range(n):
            if loads[start][end] <= m:
                sum_scores += items[end]
        answer = max(answer, sum_scores)
    
    print(answer)

if __name__ == "__main__":
    main()