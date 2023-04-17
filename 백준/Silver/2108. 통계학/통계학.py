import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
numList = [int(input()) for _ in range(N)]
print(round(sum(numList)/N))
numList.sort()
print(numList[N//2])
def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes
mostFind = modefinder(numList)
if len(mostFind) != 1:
    print(mostFind[1])
else:
    print(mostFind[0])
print(numList[-1] - numList[0])