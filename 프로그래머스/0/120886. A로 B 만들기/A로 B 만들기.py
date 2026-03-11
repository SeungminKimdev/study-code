def solution(before, after):
    words = {}
    for i in before:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    for i in after:
        if i in words:
            if words[i] == 0:
                return 0
            words[i] -= 1
        else:
            return 0
    return 1