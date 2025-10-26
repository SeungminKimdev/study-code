def solution(n, lost, reserve):
    answer = n
    new_lost = set(lost)-set(reserve)
    new_reserve = set(reserve)-set(lost)
    for loster in new_lost:
        if loster-1 in new_reserve:
            new_reserve.remove(loster-1)
        elif loster+1 in new_reserve:
            new_reserve.remove(loster+1)
        else:
            answer -= 1
    return answer