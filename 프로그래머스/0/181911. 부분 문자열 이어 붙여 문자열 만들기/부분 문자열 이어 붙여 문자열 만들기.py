def solution(my_strings, parts):
    answer = ''
    for my_string, parts, in zip(my_strings, parts):
        answer += my_string[parts[0]:parts[1]+1]
    return answer