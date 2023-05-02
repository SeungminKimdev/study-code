import sys
input = sys.stdin.readline

n = int(input())
makeAns = [0 for _ in range(n+1)]
for i in range(2, n+1):
    makeAns[i] = makeAns[i-1] + 1
    if i % 3 == 0:
        makeAns[i] = min(makeAns[i],makeAns[i//3] + 1)
    if i % 2 == 0:
        makeAns[i] = min(makeAns[i],makeAns[i//2] + 1)
print(makeAns[n])