def wordCheck(a,b):
    length = len(a)
    dif = 0
    for i in range(length):
        if a[i] != b[i]:
            dif += 1
            if dif > 1:
                return False
    if dif == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    used = [False for _ in words]
    q = [(begin,0)]
    while q:
        word,turn = q.pop()
        if word == target:
            answer = turn
            break

        for idx,i in enumerate(words):
            if not used[idx] and wordCheck(word,i):
                q.append((i,turn+1))
                used[idx] = True
    return answer