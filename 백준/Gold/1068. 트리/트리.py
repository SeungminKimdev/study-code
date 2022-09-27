import sys

class Node:
    def __init__(self):
        self.next = []
nodeList = []

N = int(input()) #노드 수
numList = list(map(int,sys.stdin.readline().split()))
cutNode = int(input())

for i in range(N):
    nodeList.append(Node())

firstNode = 0
for i in range(N):
    if numList[i] == -1:
        firstNode = i
    else:    
        nodeList[numList[i]].next.append(i)

if cutNode != firstNode: #제거 노드 제거
    nodeList[numList[cutNode]].next.remove(cutNode)
else:
    nodeList[firstNode].next = []
    
answer = 0
nextQueue = nodeList[firstNode].next
if len(nextQueue) == 0 and firstNode != cutNode: #루트노드 밖에 없는 경우
    answer = 1
while len(nextQueue) != 0:
    nextNode = nextQueue.pop(0)
    if len(nodeList[nextNode].next) == 0:
        answer += 1
    else:
        nextQueue += nodeList[nextNode].next

print(answer)
