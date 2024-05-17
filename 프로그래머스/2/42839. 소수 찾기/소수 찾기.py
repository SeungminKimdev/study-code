from itertools import permutations
import math
def solution(numbers):
    answer = 0
    numberList = list(numbers)
    numList = []
    for i in range(1,len(numbers)+1):
        npi = permutations(numberList, i)
        for n in npi:
            numList.append(int(''.join(n)))
    
    numList = list(set(numList))

    for num in numList:
        check = True
        for i in range(2,int(math.sqrt(num))+1):
            if int(num) % i == 0:
                check = False
                break
        if check and num > 1:
            answer += 1
    return answer