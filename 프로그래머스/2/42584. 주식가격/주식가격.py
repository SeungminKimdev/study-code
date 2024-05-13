def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)]
    q = [0]
    for i in range(1,len(prices)):
        while q and prices[q[-1]] > prices[i]:
            j = q.pop()
            answer[j] = i-j
        q.append(i)
    return answer