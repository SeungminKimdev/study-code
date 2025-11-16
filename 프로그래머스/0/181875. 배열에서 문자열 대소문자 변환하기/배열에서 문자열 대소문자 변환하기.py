def solution(strArr):
    for idx, s in enumerate(strArr):
        if idx % 2 == 0: # 짝수
            strArr[idx] = strArr[idx].lower()
        else: # 홀수
            strArr[idx] = strArr[idx].upper()
    return strArr