def solution(a, b, n):
    answer = 0
    bottle = n
    while bottle >= a:
        more, bottle = divmod(bottle,a)
        more *= b
        bottle += more
        answer += more
    return answer