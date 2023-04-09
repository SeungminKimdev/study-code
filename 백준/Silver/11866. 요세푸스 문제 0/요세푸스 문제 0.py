import sys
input = sys.stdin.readline

n, k = map(int,input().split())
q = [i for i in range(1,n+1)]
answer = []
while len(q) != 0:
    for _ in range(k-1):
        temp = q.pop(0)
        q.append(temp)
    answer.append(q.pop(0))
    
answerStr = "<" + str(answer[0])
for i in range(1,n):
    answerStr += ", "
    answerStr += str(answer[i])
answerStr += ">"
print(answerStr)