def solution(n, lost, reserve):
    answer = n
    new_lost = list(set(lost)-set(reserve))
    new_reserve = list(set(reserve)-set(lost))
    for loster in new_lost:
        if loster-1 in new_reserve:
            new_reserve.pop(new_reserve.index(loster-1))
        elif loster+1 in new_reserve:
            new_reserve.pop(new_reserve.index(loster+1))
        else:
            answer -= 1
    return answer