def solution(sizes):
    longer = shorter = 0
    for s1, s2 in sizes:
        if longer == 0:
            longer = max(s1, s2)
            shorter = min(s1, s2)
            continue
        longer = max(longer, max(s1, s2))
        shorter = max(shorter, min(s1, s2))
    return longer * shorter