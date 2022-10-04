N = int(input())
ans = 0
for i in range(N):
    s = input()
    check = [True for j in range(26)]
    for j in range(len(s)):
        if j < len(s) - 1:
            if s[j] != s[j+1]:
                if not check[ord(s[j])-97]:
                    ans -= 1
                    break
                else:
                    check[ord(s[j])-97] = False
        elif not check[ord(s[j])-97]:
            ans -= 1
    ans += 1
print(ans)