def solution(myString):
    answer = ''
    for word in myString:
        if word < 'l':
            answer += 'l'
        else:
            answer += word
    return answer