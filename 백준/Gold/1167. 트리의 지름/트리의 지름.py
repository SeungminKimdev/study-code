import sys
input = sys.stdin.readline

class Tree():
    def __init__(self, n):
        self.n = n
        self.tree = {}
        self.maxLen = 0
        self.maxNode = 0
        self.visited = [False] * (n+1)

    def makeTree(self):
        for _ in range(self.n):
            inputList = list(map(int,input().split()))
            now = inputList[0]
            self.tree[now] = {}
            i = 1
            while inputList[i] != -1:
                self.tree[now][inputList[i]] = inputList[i+1]
                i += 2

    def dfs(self, node, length):
        if length > self.maxLen:
            self.maxLen = length
            self.maxNode = node
        self.visited[node] = True
        
        for i in self.tree[node].keys():
            if not self.visited[i]:
                self.dfs(i,length + self.tree[node][i])
                self.visited[i] = True
    
    def makeLong(self):
        self.dfs(1,0)
        self.visited = [False] * (self.n+1)
        self.dfs(self.maxNode,0)
        print(self.maxLen)

if __name__ == '__main__':
    n = int(input())
    tree = Tree(n)
    tree.makeTree()
    tree.makeLong()