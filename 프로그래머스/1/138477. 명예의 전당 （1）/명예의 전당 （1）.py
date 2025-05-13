import heapq

def solution(k, score):
    hq = []
    answer = []
    i = 0
    
    for personal_score in score:
        if i < k:
            heapq.heappush(hq, personal_score)
            i += 1
        else:
            heapq.heappush(hq, personal_score)
            heapq.heappop(hq)
        
        min_score = heapq.heappop(hq)
        answer.append(min_score)
        heapq.heappush(hq, min_score)
        
    return answer