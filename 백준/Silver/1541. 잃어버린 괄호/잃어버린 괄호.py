import sys
input = sys.stdin.readline

n = input().strip()
ans = 0
temp = ""
check = False
for i in n:
    if check:
        if i == '+' or i == '-':
            ans -= int(temp)
            temp = ""
        else:
            temp += i
    else:
        if i == '+':
            ans += int(temp)
            temp = ""
        elif i == '-':
            check = True
            ans += int(temp)
            temp = ""
        else:
            temp += i
if check:
    ans -= int(temp)
else:
    ans += int(temp)
print(ans)