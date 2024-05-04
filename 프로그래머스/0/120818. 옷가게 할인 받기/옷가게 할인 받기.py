def solution(price):
    answer = price
    if answer >= 500000:
        answer = int(answer * 0.8)
    elif answer >= 300000:
        answer = int(answer * 0.9)
    elif answer >= 100000:
        answer = int(answer * 0.95)
    return answer