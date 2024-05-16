def solution(n, computers):
    answer = 0
    network = [0 for _ in range(n)]
    for i in range(n):
        if network[i] == 0:
            answer += 1
            q = [i]
            while q:
                now = q.pop(0)
                network[now] = 1
                for j in range(n):
                    if now != j and computers[now][j] == 1 and network[j] == 0:
                        q.append(j)  
    return answer