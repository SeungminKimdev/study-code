import heapq

def solution(scoville, K):
    hq = scoville
    heapq.heapify(hq)
    answer = 0
    while hq[0] < K:
        if len(hq) < 2:
            answer = -1
            break
        mix_food = heapq.heappop(hq)
        mix_food += heapq.heappop(hq) * 2
        heapq.heappush(hq, mix_food)
        answer += 1
    return answer