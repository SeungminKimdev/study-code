def solution(my_string, letter):
    arr_my_string = list(my_string)
    letter_idx = -1
    if letter in arr_my_string:
            letter_idx = arr_my_string.index(letter)
    while letter_idx != -1:
        arr_my_string.pop(letter_idx)
        letter_idx = -1
        if letter in arr_my_string:
            letter_idx = arr_my_string.index(letter)
    answer = "".join(arr_my_string)
    return answer