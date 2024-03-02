def solution(s):
    answer = []
    alphabet = [-1] * 26
    length = len(s)
    for i in range(length):
        alphaI = ord(s[i]) - 97
        if alphabet[alphaI] == -1:
            answer.append(-1)
        else:
            answer.append(i-alphabet[alphaI])
        alphabet[alphaI] = i
    return answer