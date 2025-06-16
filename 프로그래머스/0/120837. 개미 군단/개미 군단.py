def solution(hp):
    answer, left = divmod(hp, 5)
    soldier, left = divmod(left, 3)
    answer += soldier
    answer += left
    return answer