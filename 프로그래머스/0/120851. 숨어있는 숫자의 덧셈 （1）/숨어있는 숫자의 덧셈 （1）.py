def solution(my_string):
    answer = 0
    num_list = [str(i) for i in range(10)]
    for s in my_string:
        if s in num_list:
            answer += int(s)
    return answer