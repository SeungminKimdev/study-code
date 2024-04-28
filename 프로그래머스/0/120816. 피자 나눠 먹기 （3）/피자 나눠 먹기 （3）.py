def solution(slice, n):
    answer, b = divmod(n,slice)
    if b > 0:
        answer += 1
    return answer