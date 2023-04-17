import sys
input = sys.stdin.readline

def printQ(n,m,numList):
    q = []
    for i in range(n):
        q.append((numList[i],i))
    important = sorted(numList,reverse=True)
    answer = 1
    while len(q) != 0:
        if important[0] == q[0][0]:
            if q[0][1] == m:
                break
            important.pop(0)
            q.pop(0)
            answer += 1
        else:
            temp = q.pop(0)
            q.append(temp)
    return answer

n = int(input())
for _ in range(n):
    n,m = map(int,input().split())
    numList = [int(i) for i in input().split()]
    print(printQ(n,m,numList))