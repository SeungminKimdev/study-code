def solution(a, b, c):
    answer = 0
    check_number = len(set([a, b, c]))
    if check_number == 1:
        answer = 27 * (a ** 6)
    elif check_number == 2:
        answer = (a + b + c) * (a*a + b*b + c*c)
    else:
        answer = a + b + c
    return answer