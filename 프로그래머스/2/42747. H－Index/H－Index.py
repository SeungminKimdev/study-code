def solution(citations):
    citations.sort()
    length = len(citations)
    answer = 0
    for i in range(length,0,-1):
        if citations[length - i] >= i:
            return i
    return answer