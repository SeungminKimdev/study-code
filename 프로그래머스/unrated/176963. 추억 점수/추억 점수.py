def solution(name, yearning, photo):
    answer = []
    score = {}
    nameLen = len(name)
    
    for i in range(nameLen):
        score[name[i]] = yearning[i]
        
    for i in photo:
        ans = 0
        for j in i:
            if j in name:
                ans += score[j]
        answer.append(ans)
        
    return answer