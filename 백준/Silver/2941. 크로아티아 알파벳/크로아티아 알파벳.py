S = input()
check = ['c=','c-','d-','lj','nj','s=','z=']
fir = ['c','d','l','n','s','z']
ans = 0
i = 0
while i < len(S):
    if i <= len(S) - 2 and S[i] in fir:
        if S[i:i+2] in check:
            i += 2
        elif i <= len(S) - 3 and S[i] == 'd' and S[i+1] == 'z' and S[i+2] == '=':
            i += 3
        else:
            i += 1
    else:
        i += 1
    ans += 1
print(ans)