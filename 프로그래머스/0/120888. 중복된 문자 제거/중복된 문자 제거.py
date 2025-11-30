def solution(my_string):
    answer = ""
    check_in = []
    for s in my_string:
        if s not in check_in:
            answer += s
            check_in.append(s)
    return answer