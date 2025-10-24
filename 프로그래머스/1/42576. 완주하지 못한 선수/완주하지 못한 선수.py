def solution(participant, completion):
    from collections import Counter
    answer = list((Counter(participant) - Counter(completion)).keys())[0]
    return answer