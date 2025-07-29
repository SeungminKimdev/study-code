def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        check = numLog[i+1] - numLog[i]
        if check == 1:
            answer += 'w'
        elif check == -1:
            answer += 's'
        elif check == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer