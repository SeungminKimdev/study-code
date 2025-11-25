def solution(n):
    answer = n * 6
    for i in range(6, n*6, 6):
        if i % n == 0:
            answer = i
            break
    return answer / 6