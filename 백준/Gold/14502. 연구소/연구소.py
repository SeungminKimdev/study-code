from itertools import combinations
import copy
import sys
input = sys.stdin.readline

def bfs(arr, birus, n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = [i for i in birus]
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                queue.append((nx, ny))
    
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                count += 1
    return count

def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    walls = list(combinations(range(n*m), 3))
    birus = [(x, y) for x in range(n) for y in range(m) if arr[x][y] == 2]
    answer = 0
    
    def find_location(num):
        x = num // m
        y = num % m
        return (x, y)
    
    for wall in walls:
        wall1 = find_location(wall[0])
        if arr[wall1[0]][wall1[1]] != 0:
            continue
        wall2 = find_location(wall[1])
        if arr[wall2[0]][wall2[1]] != 0:
            continue
        wall3 = find_location(wall[2])
        if arr[wall3[0]][wall3[1]] != 0:
            continue
        
        temp_arr = copy.deepcopy(arr)
        temp_arr[wall1[0]][wall1[1]] = 1
        temp_arr[wall2[0]][wall2[1]] = 1
        temp_arr[wall3[0]][wall3[1]] = 1
        answer = max(answer, bfs(temp_arr, birus, n, m))
        del temp_arr
    
    print(answer)

if __name__ == "__main__":
	main()