def solution(n, edge):
    answer = 0
    length = [0 for _ in range(n+1)]
    graph = {i:[] for i in range(1,n+1)}
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    length[1] = 1
    
    q = [1]
    while q:
        nowNode = q.pop(0)
        for i in graph[nowNode]:
            if length[i] == 0:
                q.append(i)
                length[i] = length[nowNode] + 1
    answer = length.count(max(length))
    return answer