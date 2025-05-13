def translate(s, count, zero):
    length = len(s)
    del_zero = 0
    for i in range(length):
        if s[i] == '0':
            del_zero += 1
    next_s = str(format(length - del_zero, 'b'))
    return next_s, count + 1, zero + del_zero

def solution(s):
    x = s
    count = 0
    del_zero = 0
    while len(x) != 1:
        x, count, del_zero = translate(x, count, del_zero)
    return [count, del_zero]