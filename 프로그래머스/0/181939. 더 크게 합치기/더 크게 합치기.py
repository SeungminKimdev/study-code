def solution(a, b):
    fir = int(str(a)+str(b))
    sec = int(str(b)+str(a))
    return max(fir, sec)