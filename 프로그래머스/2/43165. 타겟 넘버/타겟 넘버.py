from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    numbers_len = len(numbers)
    for i in range(numbers_len):
        if i == 0: # 시작 queue 만들기
            q.append(numbers[i])
            q.append(numbers[i]*-1)
            continue
        if i == numbers_len-1: # 마지막 조건 확인
            while q:
                number = q.popleft()
                if number + numbers[i] == target or number - numbers[i] == target:
                    answer += 1
            continue
        
        # BFS 루트
        q_len = len(q)
        for _ in range(q_len):
            number = q.popleft()
            next_number_plus = number + numbers[i]
            next_number_minus = number - numbers[i]
            if abs(target - next_number_plus) <= 50 * (numbers_len - i - 1):
                q.append(next_number_plus)
            if abs(target - next_number_minus) <= 50 * (numbers_len - i - 1):
                q.append(next_number_minus)
    return answer