def solution(sides):
    sides = sorted(sides)
    if sides[2] < sides[1] + sides[0]:
        return 1
    else:
        return 2
    return answer