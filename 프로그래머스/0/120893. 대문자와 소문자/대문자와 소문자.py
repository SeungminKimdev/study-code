def solution(my_string):
    answer = ''
    for s in my_string:
        if s < 'a':
            answer += s.lower()
        else:
            answer += s.upper()
    return answer