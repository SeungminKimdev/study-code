import sys
input = sys.stdin.readline

def spread_dust(room, R, C):
    new_room = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:  # 먼지가 있는 경우
                spread_amount = room[i][j] // 5
                spread_count = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        new_room[nx][ny] += spread_amount
                        spread_count += 1
                new_room[i][j] += room[i][j] - (spread_amount * spread_count)
            elif room[i][j] == -1:  # 공기청정기 위치
                new_room[i][j] = -1
    return new_room

def purify_air(room, upper, lower, R, C):
    # 위쪽 공기청정기 (반시계 방향)
    for i in range(upper - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    for i in range(C - 1):
        room[0][i] = room[0][i + 1]
    for i in range(upper):
        room[i][C - 1] = room[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        room[upper][i] = room[upper][i - 1]
    room[upper][1] = 0

    # 아래쪽 공기청정기 (시계 방향)
    for i in range(lower + 1, R - 1):
        room[i][0] = room[i + 1][0]
    for i in range(C - 1):
        room[R - 1][i] = room[R - 1][i + 1]
    for i in range(R - 1, lower, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        room[lower][i] = room[lower][i - 1]
    room[lower][1] = 0

def main():
    R, C, T = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(R)]

    # 공기청정기 위치 찾기
    purifier = []
    for i in range(R):
        if room[i][0] == -1:
            purifier.append(i)

    upper, lower = purifier

    # 시뮬레이션
    for _ in range(T):
        room = spread_dust(room, R, C)  # 미세먼지 확산
        purify_air(room, upper, lower, R, C)  # 공기청정기 작동

    # 남아있는 미세먼지의 총량 계산
    total_dust = sum(sum(cell for cell in row if cell > 0) for row in room)
    print(total_dust)

if __name__ == "__main__":
    main()