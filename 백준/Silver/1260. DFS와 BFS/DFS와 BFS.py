class Node:
    def __init__(self,num):
        self.number = num
        self.next = []
        
class Tree:
    def __init__(self, num):
        self.size = num
        self.nodeList = [Node(i) for i in range(num)]
        self.visited = [False for i in range(self.size)]
    def addNode(self,a,b):
        self.nodeList[a-1].next.append(b-1)
        self.nodeList[a-1].next.sort()
        self.nodeList[b-1].next.append(a-1)
        self.nodeList[b-1].next.sort()
    def resetVisit(self):
        self.visited = [False for i in range(self.size)]
    def bfs(self,nodeNum):
        queue = []
        queue.append(self.nodeList[nodeNum])
        self.visited[nodeNum] = True
        answer = ''
        while len(queue) != 0:
            tempnode = queue.pop(0)
            answer += str(tempnode.number+1)
            answer += ' '
            for i in tempnode.next:
                if not self.visited[i]:
                    queue.append(self.nodeList[i])
                    self.visited[i] = True
        print(answer[:-1])
    def dfs(self,nodeNum):
        node = self.nodeList[nodeNum]
        answer = [node.number+1]
        self.visited[node.number] = True
        for i in node.next:
            if not self.visited[i]:
                self.visited[i] = True
                answer += self.dfs(i)
        return answer
    
N, M, V = map(int,input().split())
tree = Tree(N)
for i in range(M):
    a, b = map(int,input().split())
    tree.addNode(a,b)
answer = ''
for i in tree.dfs(V-1):
    answer += str(i)
    answer += ' '
print(answer[:-1])
tree.resetVisit()
tree.bfs(V-1)