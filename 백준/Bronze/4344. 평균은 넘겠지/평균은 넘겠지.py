C = int(input())
for i in range(C):
    numList = list(map(int,input().split()))
    N = numList.pop(0)
    avg = sum(numList) / float(N)
    ans = 0
    for j in numList:
        if j > avg:
            ans += 1
    print('{:.3f}%'.format((ans * 100) / float(N)))