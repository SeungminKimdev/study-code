import sys
input = sys.stdin.readline

def check(a, b, numa, numb):
    num = 0
    for i in range(numa,numa+8):
        for j in range(numb,numb+8):
            if a[i][j] != b[i-numa][j-numb]:
                num += 1
    return min(num, 64-num)

checkword = ['WBWBWBWB','BWBWBWBW'] * 4

n, m = map(int, input().split())
inputword = []
for _ in range(n):
    inputword.append(str(input().strip()))
    
answer = 64
for i in range(0,n-7):
    for j in range(0,m-7):
        answer = min(answer,check(inputword,checkword,i,j))
print(answer)