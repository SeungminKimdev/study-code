import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
str1len = len(str1) + 1
str2len = len(str2) + 1
lcs = {i:[0]*str2len for i in range(str1len)}

for i in range(1,str1len):
    for j in range(1,str2len):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
            
ans = lcs[str1len-1][str2len-1]
print(ans)
if ans != 0:
    anstr = ''
    for i in range(str1len-1,0,-1):
        for j in range(str2len-1,0,-1):
            temp = lcs[i][j]
            if temp == 0:
                break
            if temp == lcs[i][j-1]:
                continue
            elif temp == lcs[i-1][j]:
                break
            else:
                anstr += str1[i-1]
                str2len = j
                break
    print(anstr[::-1])