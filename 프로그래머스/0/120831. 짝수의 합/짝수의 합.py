def solution(n):
    if n % 2 == 0:
        answer = (2+n)*(n//2)/2
    else:
        answer = (2+n-1)*(n//2)/2
    return answer