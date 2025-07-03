def solution(my_string, num1, num2):
    answer = ''
    for i in range(len(my_string)):
        if i == min(num1, num2):
            answer += my_string[max(num1,num2)]
        elif i == max(num1, num2):
            answer += my_string[min(num1,num2)]
        else:
            answer += my_string[i]
    return answer