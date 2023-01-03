import sys

n = int(sys.stdin.readline())
nodes = int(sys.stdin.readline())

computer = [[] for _ in range(n)] #연결 노드 번호
virus = [False for _ in range(n)] #감염여부

for _ in range(nodes):
    a, b = map(int, sys.stdin.readline().split())
    computer[a-1].append(b-1)
    computer[b-1].append(a-1)
    
virus[0] = True
queue = [0]
answerNum = 0

while(len(queue) != 0):
    tempNum = queue.pop(0)
    for i in computer[tempNum]:
        if(not virus[i]):
            queue.append(i)
            virus[i] = True
            answerNum += 1
            
print(answerNum)