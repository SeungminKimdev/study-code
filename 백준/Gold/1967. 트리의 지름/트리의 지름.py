import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Tree():
    def __init__(self,n):
        self.N = n
        self.tree = {}
        for _ in range(n-1):
            a, b, c = map(int,input().split())
            if a in self.tree:
                self.tree[a].append((b,c))
            else:
                self.tree[a] = [(b,c)]
            if b in self.tree:
                self.tree[b].append((a,c))
            else:
                self.tree[b] = [(a,c)]
        self.visited = [False]*(n+1)
        self.dis = [0] * (n+1)
    def dfs(self,num):
        self.visited[num] = True
        for i in self.tree[num]:
            if not self.visited[i[0]]:
                self.dis[i[0]] = self.dis[num] + i[1]
                self.dfs(i[0])
    def makeAns(self):
        self.dfs(1)
        maxNode = self.dis.index(max(self.dis))
        self.visited = [False] * (self.N+1)
        self.dis = [0] * (self.N+1)
        self.dfs(maxNode)
        print(max(self.dis))

def solution():
    n = int(input())
    if n == 1:
        print('0')
        return
    tree = Tree(n)
    tree.makeAns()
    
if __name__ == '__main__':
    solution()