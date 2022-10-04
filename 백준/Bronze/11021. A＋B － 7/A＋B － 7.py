N = int(input())
for i in range(N):
    answer = sum(map(int,input().split()))
    print('Case #%d: %d'%(i+1,answer))