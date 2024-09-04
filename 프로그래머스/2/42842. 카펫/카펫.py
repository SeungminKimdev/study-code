def solution(brown, yellow):
    answer = []
    xMin = int(yellow ** 0.5)
    for i in range(xMin, yellow+1):
        a, b = divmod(yellow,i)
        if b == 0 and (i+a)*2+4 == brown:
            answer = [i+2,a+2]
    return answer