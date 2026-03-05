def solution(myString, pat):
    answer = 0
    l = len(myString)
    p = len(pat)
    for i in range(0, l-p+1, 1):
        if myString[i:i+p] == pat:
            answer += 1
    return answer