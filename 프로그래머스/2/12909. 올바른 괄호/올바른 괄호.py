def solution(s):
    opened = 0
    for c in s:
        if c == "(":
            opened += 1
        elif opened:
            opened -= 1
        else:
            return False
    if opened:
        return False
    return True