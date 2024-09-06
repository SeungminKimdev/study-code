import heapq

def solution(operations):
    minQ = []
    maxQ = []
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            heapq.heappush(minQ,num)
            heapq.heappush(maxQ,-num)
        else:
            if num == 1 and maxQ:
                popNum = -heapq.heappop(maxQ)
                minQ.pop(minQ.index(popNum))
            elif num == -1 and minQ:
                popNum = -heapq.heappop(minQ)
                maxQ.pop(maxQ.index(popNum))
    if minQ:
        answer = [-heapq.heappop(maxQ),heapq.heappop(minQ)]
    else:
        answer = [0,0]
                
    return answer