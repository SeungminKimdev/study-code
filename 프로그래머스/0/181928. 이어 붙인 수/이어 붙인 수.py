def solution(num_list):
    answer = 0
    num1 = 0
    num2 = 0
    for num in num_list:
        if num % 2 == 0:
            num1 *= 10
            num1 += num
        else:
            num2 *= 10
            num2 += num
    answer = num1 + num2
    return answer