def solution(n, results):
    answer = 0
    wingraph = {i:[] for i in range(n+1)}
    losegraph = {i:[] for i in range(n+1)}
    for a,b in results:
        wingraph[a].append(b)
        losegraph[b].append(a)
        
    for i in range(1,n+1):
        node = 1
        q = [] + wingraph[i]
        visited = [False for _ in range(n+1)]
        visited[i] = True
        
        while q:
            now = q.pop(0)
            if visited[now]:
                continue
            visited[now] = True
            node += 1
            q += wingraph[now]
            
        q = [] + losegraph[i]
        while q:
            now = q.pop(0)
            if visited[now]:
                continue
            visited[now] = True
            node += 1
            q += losegraph[now]

        if node == n:
            answer += 1          
    return answer