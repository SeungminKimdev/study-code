import re

def solution(myStr):
    answer = re.split("a|b|c", myStr)
    answer = ' '.join(answer).split()
    if len(answer) == 0:
        answer = ["EMPTY"]
    return answer