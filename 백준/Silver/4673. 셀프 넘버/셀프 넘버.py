def d(n):
    ans = n
    while n > 0:
        ans += n % 10
        n //= 10
    return ans
numList = [True for i in range(10001)]
for i in range(1,10001):
    if numList[i]:
        print(i)
        check = i
        while True:
            check = d(check)
            if check > 10000 or not numList[check]:
                break
            else:
                numList[check] = False