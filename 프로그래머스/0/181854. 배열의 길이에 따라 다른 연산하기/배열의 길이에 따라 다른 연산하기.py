def solution(arr, n):
    arr_length = len(arr)
    fir_idx = 0
    if arr_length % 2 == 0: # 짝수
        fir_idx = 1
    for i in range(fir_idx, arr_length, 2):
        arr[i] += n
    return arr