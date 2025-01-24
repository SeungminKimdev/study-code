from collections import deque
import sys
input = sys.stdin.readline

def out_of_air(air): # 외부 공기 표시
    global n, m, page, dx, dy
    q = deque(air)
    while q:
        x, y = q.popleft()
        page[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and page[nx][ny] == 0:
                page[nx][ny] = 2
                q.append((nx, ny))

def main():
    global n, m, page, dx, dy
    n, m = map(int, input().split())
    page = [list(map(int, input().split())) for _ in range(n)]
    time = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    # 외부 공기 초기 좌표
    air = [(0,0)]
    # 치즈 좌표 저장
    cheese = [(i,j) for i in range(n) for j in range(m) if page[i][j] == 1]
    
    while cheese:
        out_of_air(air)
        
        air.clear()
        new_cheese = []
        
        for x, y in cheese:
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and page[nx][ny] == 2:
                    cnt += 1
            if cnt >= 2:
                air.append((x, y))
                page[x][y] = 0
            else:
                new_cheese.append((x, y))
        cheese = new_cheese
        time += 1
    
    print(time)

if __name__ == "__main__":
    main()