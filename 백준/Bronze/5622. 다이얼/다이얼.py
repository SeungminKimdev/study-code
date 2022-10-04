num = input()
ans = 0
for i in [ord(j)-65 for j in num]:
    ans += 2
    if i < 3:
        ans += 1
    elif i < 6:
        ans += 2
    elif i < 9:
        ans += 3
    elif i < 12:
        ans += 4
    elif i < 15:
        ans += 5
    elif i < 19:
        ans += 6
    elif i < 22:
        ans += 7
    else:
        ans += 8
print(ans)