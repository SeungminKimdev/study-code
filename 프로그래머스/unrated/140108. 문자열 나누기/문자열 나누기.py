def solution(s):
    answer = 0
    firNum = 0
    otherNum = 0
    for i in range(len(s)):
        if firNum == 0:
            fir = s[i]
            firNum += 1
        elif fir == s[i]:
            firNum += 1
        else:
            otherNum += 1
            
        if firNum == otherNum:
            answer += 1
            firNum = 0
            otherNum = 0
    if firNum != 0:
        answer += 1
    return answer