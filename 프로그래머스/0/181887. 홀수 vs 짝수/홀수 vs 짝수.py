def solution(num_list):
    even, odd = 0, 0
    for idx, num in enumerate(num_list):
        if idx % 2 == 1:
            even += num
        else:
            odd += num
    answer = even
    if even < odd:
        answer = odd
    return answer