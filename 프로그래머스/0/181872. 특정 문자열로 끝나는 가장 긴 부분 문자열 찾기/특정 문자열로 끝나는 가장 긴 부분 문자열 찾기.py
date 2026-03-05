def solution(myString, pat):
    pat_length = len(pat)
    str_length = len(myString)
    for i in range(str_length-pat_length, -1, -1):
        if myString[i:i+pat_length] == pat:
            answer = myString[:i+pat_length]
            break
    return answer