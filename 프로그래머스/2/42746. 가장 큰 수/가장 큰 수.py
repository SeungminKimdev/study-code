def solution(numbers):
    answer = ''
    str_numbers = list(map(str,numbers))
    str_numbers.sort(key=lambda x:x*3, reverse=True)
    for i in str_numbers:
        if answer == '0' and i == '0':
            break
        else:
            answer += i
    return answer