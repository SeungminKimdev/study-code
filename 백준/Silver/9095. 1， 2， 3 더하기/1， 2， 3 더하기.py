import sys
input = sys.stdin.readline

n = int(input())
ans = [0]*11
ans[1] = 1
ans[2] = 2
ans[3] = 4
for i in range(4,11):
    ans[i] = ans[i-1] + ans[i-2] + ans[i-3]
    
for _ in range(n):
    print(ans[int(input())])