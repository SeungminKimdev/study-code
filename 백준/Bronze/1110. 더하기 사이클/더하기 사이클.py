import copy
N = int(input())
check = 1
newNum = copy.copy(N)
if newNum < 10:
    newNum *= 11
else:
    newNum = (newNum % 10) * 10 + sum(divmod(newNum,10)) % 10
while N != newNum:
    if newNum < 10:
        newNum *= 11
    else:
        newNum = (newNum % 10) * 10 + sum(divmod(newNum,10)) % 10
    check += 1
print(check)