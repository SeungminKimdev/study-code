import sys
input = sys.stdin.readline

weight = int(input())

if weight % 5 == 0:
    print(weight // 5)
else:
    sum = 0
    while weight > 0:
        weight -= 3
        sum += 1
        if weight % 5 == 0:
            sum += weight // 5
            print(sum)
            break
        elif weight < 3:
            print(-1)
            break
        elif weight == 0:
            print(sum)
            break