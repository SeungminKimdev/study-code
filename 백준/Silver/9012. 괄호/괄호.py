import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    string = input().strip()
    check = []
    temp = 0
    for i in string:
        if i == "(":
            check.append(i)
        else:
            if len(check) == 0:
                temp = 1
                break
            else:
                check.pop()
    if len(check) == 0 and temp == 0:
        print("YES")
    else:
        print("NO")