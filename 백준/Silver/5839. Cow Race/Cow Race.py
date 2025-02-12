import sys
input = sys.stdin.readline

def main():
    # 입력 데이터 처리
    N, M = map(int, input().split())
    bessie_segments = []
    for _ in range(N):
        speed, duration = map(int, input().split())
        bessie_segments.append((speed, duration))
    elsie_segments = []
    for _ in range(M):
        speed, duration = map(int, input().split())
        elsie_segments.append((speed, duration))
    
    # 시뮬레이션 초기화
    b_index, e_index = 0, 0  # 현재 구간 인덱스
    b_speed, b_time_left = bessie_segments[b_index]
    e_speed, e_time_left = elsie_segments[e_index]
    b_pos, e_pos = 0, 0  # 두 소의 누적 이동 거리
    last_leader = None  # 마지막으로 선두였던 소 ('B' 또는 'E'). 초반에는 동점 상태로 None.
    lead_changes = 0

    # 전체 경주 시간 (두 소 모두 동일한 총 달린 시간)
    total_time = sum(duration for _, duration in bessie_segments)
    
    # 매 단위 시간마다 시뮬레이션 진행
    for _ in range(total_time):
        # 현재 속도로 각 소의 누적 거리를 갱신
        b_pos += b_speed
        e_pos += e_speed

        # 현재 구간의 남은 시간 감소
        b_time_left -= 1
        e_time_left -= 1

        # Bessie의 구간이 끝났다면 다음 구간으로 이동
        if b_time_left == 0 and b_index < N - 1:
            b_index += 1
            b_speed, b_time_left = bessie_segments[b_index]
        
        # Elsie의 구간이 끝났다면 다음 구간으로 이동
        if e_time_left == 0 and e_index < M - 1:
            e_index += 1
            e_speed, e_time_left = elsie_segments[e_index]
        
        # 현재 선두 상태 결정 (동점이면 None 처리)
        if b_pos > e_pos:
            current_leader = 'B'
        elif e_pos > b_pos:
            current_leader = 'E'
        else:
            current_leader = None
        
        # 선두 변경 체크: 마지막으로 선두였던 소와 다르면 리더십 체인지 발생
        if current_leader is not None:
            if last_leader is not None and current_leader != last_leader:
                lead_changes += 1
            last_leader = current_leader

    # 결과 출력
    print(lead_changes)

if __name__ == "__main__":
    main()