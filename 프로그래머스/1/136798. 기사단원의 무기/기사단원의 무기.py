import math

def solution(number, limit, power):
    answer = 1
    for i in range(2, number+1):
        measure = 0
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                if j ** 2 == i:
                    measure += 1
                else:
                    measure += 2
                if measure > limit:
                    answer += power
                    break
        if measure <= limit:
            answer += measure
    return answer