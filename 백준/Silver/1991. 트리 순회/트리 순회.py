#백준 1991
import sys
input = sys.stdin.readline

def before(nodeName): #전위순회
    if nodeName != ".":
        fir, sec = tree[nodeName]
        if fir != ".":
            nodeName += before(fir)
        if sec != ".":
            nodeName += before(sec)
        return nodeName
    
def middle(nodeName): #중위순회
    if nodeName != ".":
        fir, sec = tree[nodeName]
        if fir != ".":
            nodeName = middle(fir) + nodeName
        if sec != ".":
            nodeName += middle(sec)
        return nodeName

def last(nodeName): #후위 순회
    if nodeName != ".":
        fir, sec = tree[nodeName]
        answer = ""
        if fir != ".":
            answer += last(fir)
        if sec != ".":
            answer += last(sec)
        answer += nodeName
        return answer

N = int(input())
tree = {}
for _ in range(N):
    pNode, c1Node, c2Node = input().split()
    tree[pNode] = [c1Node, c2Node]

print(before("A"))
print(middle("A"))
print(last("A"))