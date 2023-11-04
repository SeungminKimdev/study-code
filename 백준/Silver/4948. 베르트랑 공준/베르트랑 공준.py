import sys
input = sys.stdin.readline

if __name__ == '__main__':
    sosu = []
    for i in range(2,123456*2+1):
        find = True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                find = False
                break
        if find:
            sosu.append(i)
    while 1:
        n = int(input())
        if n == 0:
            break
        ans = 0
        for i in sosu:
            if i > n and i <= 2*n:
                ans += 1
            elif i > 2*n:
                break
        print(ans)