def solution(arr, k):
    def mul(num):
        return num * k
    def add(num):
        return num + k
    if k % 2 == 0:
        answer = list(map(add, arr))
    else:
        answer = list(map(mul, arr))
    return answer