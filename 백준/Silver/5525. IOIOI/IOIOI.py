import sys
input = sys.stdin.readline

def howmany(inputS,n):
    checking = "I" + "OI" * n
    check = inputS.find(checking,0)
    ans = 0
    while check != -1:
        ans += 1
        check = inputS.find(checking,check+2)
    return ans

n = int(input())
m = int(input())
inputS = input().strip()
print(howmany(inputS,n))