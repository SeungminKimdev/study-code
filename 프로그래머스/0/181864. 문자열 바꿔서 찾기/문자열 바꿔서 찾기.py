def solution(myString, pat):
    answer = 0
    change = ['A', 'B']
    changeString = ''
    for s in myString:
        changeString += change[int(s == 'A')]
    answer = int(pat in changeString)
    return answer