import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break
    
    ans = 1
    temp = 1
    while True:
        if temp % n == 0:
            print(ans)
            break
        ans += 1
        temp *= 10
        temp += 1