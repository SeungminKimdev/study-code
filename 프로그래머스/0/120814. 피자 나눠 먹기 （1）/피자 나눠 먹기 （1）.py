def solution(n):
    answer,b = divmod(n,7)
    if b != 0:
        answer += 1
    return answer