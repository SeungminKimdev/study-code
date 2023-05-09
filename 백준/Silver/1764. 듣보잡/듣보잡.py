import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nList = {input().strip():True for _ in range(n)}

ans = []
for _ in range(m):
    inputM = input().strip()
    try:
        if nList[inputM]:
            ans.append(inputM)
    except:
        continue
    
print(len(ans))
if ans != 0:
    ans.sort()
    print(*ans, sep = '\n')