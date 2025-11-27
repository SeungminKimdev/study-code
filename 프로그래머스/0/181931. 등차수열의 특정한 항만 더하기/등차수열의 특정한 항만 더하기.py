def solution(a, d, included):
    answer = 0
    stack_num = 0
    for next_sum in included:
        if stack_num == 0:
            stack_num += a
        else:
            stack_num += d
        if next_sum:
            answer += stack_num
    return answer