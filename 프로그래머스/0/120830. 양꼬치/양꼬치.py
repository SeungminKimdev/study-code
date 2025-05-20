LAMB = 12000
DRINK = 2000

def solution(n, k):
    answer = 0
    answer += LAMB * n
    paid_drink = k - n // 10
    if paid_drink > 0:
        answer += DRINK * paid_drink
    return answer