def check(n):
    if n < 10:
        return True
    else:
        length = len(str(n))
        fir = int(str(n)[0])
        term = fir - int(str(n)[1])
        for i in range(1,length):
            temp = int(str(n)[i])
            if fir - temp != term:
                return False
            fir = temp
        return True
N = int(input())
ans = 0
for i in range(1,N+1):
    if check(i):
        ans += 1
print(ans)