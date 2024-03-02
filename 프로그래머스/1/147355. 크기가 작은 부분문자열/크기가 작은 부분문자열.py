def solution(t, p):
    answer = 0
    pLen = len(p)
    tLen = len(t)
    for i in range(tLen-pLen+1):
        if int(p) >= int(t[i:i+pLen]):
            answer += 1
    return answer