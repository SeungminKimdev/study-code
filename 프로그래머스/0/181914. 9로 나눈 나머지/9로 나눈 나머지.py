def solution(number):
    answer = sum(map(int,list(number))) % 9
    return answer