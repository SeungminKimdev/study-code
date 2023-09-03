import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    alpha = {}
    for _ in range(n):
        inStr = input().rstrip()
        length = len(inStr)
        for i in range(length):
            if inStr[i] in alpha:
                alpha[inStr[i]] += 10**(length-i-1)
            else:
                alpha[inStr[i]] = 10**(length-i-1)
    alpha = sorted(alpha.items(), key = lambda x : x[1], reverse=True)
    num = 9
    ans = 0
    for i in alpha:
        ans += i[1] * num
        num -= 1
    print(ans)
if __name__ == '__main__':
    solution()