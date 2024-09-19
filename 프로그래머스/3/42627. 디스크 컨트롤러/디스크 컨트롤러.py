import heapq

def solution(jobs):
    heap = []
    answer = 0
    now = 0
    jobs = sorted(jobs)
    
    for job in jobs:
        while heap and job[0] > now:
            workTime, startTime = heapq.heappop(heap)
            now += workTime
            answer += (now - startTime)
        
        heapq.heappush(heap, (job[1],job[0]))
        
        if job[0] > now and heap:
            now = job[0]

    while heap:
        workTime, startTime = heapq.heappop(heap)
        now += workTime
        answer += (now - startTime)
    return int(answer / len(jobs))