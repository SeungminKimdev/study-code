import sys

N, K = map(int, sys.stdin.readline().split()) #N = 물품 수, K = 한계 무게
items = [] #물품 정보
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split()) #W = 무게, V = 가치
    items.append([W,V])

bag = [[0 for _ in range(N+1)] for _ in range(K+1)] #총 가치를 저장
for i in range(1,K+1): #무게 증가
    for j in range(1,N+1): #물품 수 증가
        bag[i][j] = bag[i][j-1]
        if(items[j-1][0] <= i):
            bag[i][j] = max(bag[i][j],bag[i-items[j-1][0]][j-1] + items[j-1][1]) #더 큰 가치를 저장
            
print(bag[K][N])