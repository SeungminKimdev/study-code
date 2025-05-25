def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = my_string
    for vowel in vowels:
        answer = answer.replace(vowel, '')
    return answer