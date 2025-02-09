from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    passengers = deque([int(input()) for _ in range(n)])
    seat_used = [False] * 1001  # 1번 ~ 1000번 행(복도)
    corridor = deque()
    turn = 0
    
    if passengers:
        corridor.append((passengers.popleft(), 1, 0))  # (목표행, 현재행, 짐정리 경과시간)
        seat_used[1] = True

    while corridor or passengers:
        if passengers and not seat_used[1]:
            corridor.append((passengers.popleft(), 1, 0))
            seat_used[1] = True

        temp = len(corridor)
        for _ in range(temp):
            target_loc, now_loc, baggage_time = corridor.popleft()
            if baggage_time == 4: # 짐 정리를 끝낸 고객
                seat_used[now_loc] = False
                continue

            if target_loc == now_loc:
                baggage_time += 1
                corridor.append((target_loc, now_loc, baggage_time))
            else:
                if not seat_used[now_loc+1]:
                    seat_used[now_loc+1] = True
                    seat_used[now_loc] = False
                    now_loc += 1
                corridor.append((target_loc, now_loc, baggage_time))
        turn += 1

    print(turn)

if __name__ == "__main__":
    main()
