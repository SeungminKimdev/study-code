import sys
input = sys.stdin.readline

n = int(input())
inputTime = []
for _ in range(n):
    start, end = map(int,input().split())
    inputTime.append((end,start))
inputTime.sort()
now = 0
ans = 0
for i in inputTime:
    if i[1] >= now:
        now = i[0]
        ans += 1
    else:
        continue
print(ans)