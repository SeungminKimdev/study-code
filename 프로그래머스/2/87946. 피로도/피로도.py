def solution(k, dungeons):
    answer = -1
    q = [(k,[],0)]
    while q:
        health, visited, clear = q.pop(0)
        answer = max(answer, clear)
        for i in range(len(dungeons)):
            if i not in visited and dungeons[i][0] <= health:
                q.append(((health - dungeons[i][1]),visited + [i],clear+1))
    return answer