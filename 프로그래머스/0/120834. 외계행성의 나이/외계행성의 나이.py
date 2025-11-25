def solution(age):
    answer = ''
    for s in list(str(age)):
        answer += chr(ord('a') + int(s))
    return answer