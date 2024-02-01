import sys
input = sys.stdin.readline

def findP(parent,x):
    if x != parent[x]:
        parent[x] = findP(parent,parent[x])
        return parent[x]
    else:
        return parent[x]
    
def mergeP(parent,x,y):
    px = findP(parent,x)
    py = findP(parent,y)
    if px != py:
        if px > py:
            parent[px] = parent[py]
        else:
            parent[py] = parent[px]

n,m = map(int,input().split())
know = list(map(int,input().split()))
parent = [i for i in range(51)]
if know[0] != 0:
    for i in know[1:]:
        parent[i] = 0
party = []
for i in range(m):
    party.append(list(map(int,input().split())))
    for j in range(2,party[i][0]+1):
        mergeP(parent,party[i][1],party[i][j])

answer = m
for i in party:
    for j in range(1,i[0]+1):
        if findP(parent,i[j]) == 0:
            answer -= 1
            break
print(answer)