n1 = int(input())

for _ in range(n1):
    n2 = int(input())
    best, bestNum = input().split()
    bestNum = int(bestNum)
    for _ in range(n2-1):
        school, num = input().split()
        num = int(num)
        if num > bestNum:
            best = school
            bestNum = num
    print(best)