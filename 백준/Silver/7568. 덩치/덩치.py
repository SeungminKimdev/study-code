import sys
input = sys.stdin.readline

n = int(input())
people = []
rankP = [0] * n
for _ in range(n):
    x, y = map(int,input().split())
    people.append((x,y))

for i in range(n):
    for j in people:
        if people[i][0] < j[0] and people[i][1] < j[1]:
            rankP[i] += 1
    rankP[i] += 1
print(*rankP)