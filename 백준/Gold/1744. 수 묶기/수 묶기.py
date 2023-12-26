import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
n -= 1
arr.sort()
ans = 0
i = 0
while i < n:
    if arr[i] < 0 and arr[i+1] <= 0:
        ans += arr[i] * arr[i+1]
        i += 2
    else:
        break
while n > i:
    if arr[n] > 1 and arr[n-1] > 1:
        ans += arr[n] * arr[n-1]
        n -= 2
    else:
        break
for t in range(i,n+1):
    ans += arr[t]
print(ans)