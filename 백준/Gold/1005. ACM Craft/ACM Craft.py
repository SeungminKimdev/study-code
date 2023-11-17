import sys
input = sys.stdin.readline

testCase = int(input())
for _ in range(testCase):
    n, k = map(int,input().split())
    cost = list(map(int,input().split()))
    lenPre = [0] * (n+1)
    timeSum = [0] * (n+1)
    need = {}
    for _ in range(k):
        x,y = map(int,input().split())
        lenPre[y] += 1
        if x in need:
            need[x].append(y)
        else:
            need[x] = [y]
    target = int(input())
    q=[]
    for i in range(1,n+1):
        if lenPre[i] == 0:
            q.append(i)
    
    while lenPre[target] > 0:
        now = q.pop()
        if now not in need:
            continue
        for i in need[now]:
            timeSum[i] = max(timeSum[i],cost[now-1]+timeSum[now])
            lenPre[i] -= 1
            if lenPre[i] == 0:
                q.append(i)
    print(timeSum[target] + cost[target-1])