def solution(i, j, k):
    answer = 0
    for num in range(i, j+1, 1):
        if str(k) in str(num):
            for s in str(num):
                if s == str(k):
                    answer += 1
    return answer