import sys
input = sys.stdin.readline

def main():
    str1 = list(input().rstrip())
    str2 = list(input().rstrip())
    str1Len = len(str1)
    str2Len = len(str2)
    lcs = {i:[0]*(str1Len+1) for i in range(str2Len+1)}
    for i in range(1,str2Len+1):
        for j in range(1,str1Len+1):
            if str1[j-1] == str2[i-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
    print(lcs[str2Len][str1Len])
    return

if __name__ == "__main__":
    main()