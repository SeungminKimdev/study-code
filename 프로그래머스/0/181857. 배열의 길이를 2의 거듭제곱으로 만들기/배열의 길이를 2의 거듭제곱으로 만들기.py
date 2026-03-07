def solution(arr):
    arr_length = len(arr)
    zeros = 1
    while zeros < arr_length:
        zeros *= 2
    answer = arr
    answer += [0] * (zeros - arr_length)
    return answer