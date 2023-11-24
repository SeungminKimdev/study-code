import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    testCase = input().split()
    num = float(testCase[0])
    for i in range(1,len(testCase)):
        if testCase[i] == '@':
            num *= 3
        elif testCase[i] == '%':
            num += 5
        else:
            num -= 7
    print('{:.2f}'.format(num))