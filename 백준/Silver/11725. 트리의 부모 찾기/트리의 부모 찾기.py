#백준 1012
import sys
input = sys.stdin.readline

n = int(input())
tree = [[-1] for _ in range(n)]
answer = [-1] * n

for _ in range(1,n):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

visited = [False] * n
visited[0] = True
queue = [0]
while len(queue) != 0:
    head = queue.pop(0)
    nextList = tree[head]
    for i in nextList:
        if i == -1:
            continue
        if not visited[i]:
            answer[i] = head
            queue.append(i)
            visited[i] = True
answer.pop(0)
for i in answer:
    print(i+1)