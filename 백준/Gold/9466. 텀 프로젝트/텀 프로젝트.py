import sys
input = sys.stdin.readline

def solution(n, arr):
    visited = [0] * n
    isCycle = [0] * n
    
    def dfs(node):
        path = []
        while True:
            if visited[node]:
                if node in path:
                    startNode = path.index(node)
                    for i in range(startNode, len(path)):
                        isCycle[path[i]] = 1
                return
            visited[node] = 1
            path.append(node)
            node = arr[node] - 1
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return n - sum(isCycle)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solution(n, arr))

if __name__ == "__main__":
	main()