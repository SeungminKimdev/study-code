from itertools import combinations

def solution(number):
    answer = 0
    nC3 = combinations(number,3)
    for i in nC3:
        if sum(i) == 0:
            answer += 1
    return answer