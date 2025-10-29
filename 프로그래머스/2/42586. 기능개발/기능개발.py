from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque()
    for progress, speed in zip(progresses, speeds):
        q.append((progress, speed))
    while q:
        finish = 0
        before_finish = 0 # 직전 작업 완료 여부 [0, 1]
        q_length = len(q)
        # 가장 앞의 기능 확인
        next_progress, speed = q.popleft()
        next_progress += speed
        if next_progress >= 100:
            finish += 1
            before_finish = 1
        else:
            q.append((next_progress, speed))
        # 그 다음 모든 작업 확인
        for _ in range(q_length-1):
            next_progress, speed = q.popleft()
            next_progress += speed
            if before_finish and next_progress >= 100:
                finish += 1
                before_finish = 1
                continue
            q.append((next_progress, speed))
            before_finish = 0
        if finish:
            answer.append(finish)
    return answer