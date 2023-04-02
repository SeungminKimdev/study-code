import sys
input = sys.stdin.readline

n = int(input())

ageDict = {}
ageArr = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    if ageDict.get(age) == None:
        ageDict[age] = [name]
    else:
        ageDict[age].append(name)
    ageArr.append(age)
ageArr.sort()
ageArr = set(ageArr)
for i in ageArr:
    for j in ageDict[i]:
        print(str(i) + " " + j)