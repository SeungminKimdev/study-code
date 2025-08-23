def solution(num, k):
    answer = 0
    try:
        answer = str(num).index(str(k)) + 1
    except:
        answer = -1
    return answer