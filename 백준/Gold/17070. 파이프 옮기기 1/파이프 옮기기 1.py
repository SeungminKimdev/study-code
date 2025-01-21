import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    answer = 0
    q = [(0, 0, 0, 1, 0)] # x1, y1, x2, y2, 파이프 모양
    
    while q:
        x1, y1, x2, y2, shape = q.pop()
        if x2 == n-1 and y2 == n-1 and arr[x2][y2] == '0':
            answer += 1
            continue
        if shape == 0 and y2 + 1 < n: # 가로
            if arr[x2][y2+1] == '0':
                q.append((x2, y2, x2, y2+1, 0))
                if x2 + 1 < n and arr[x2+1][y2] == '0' and arr[x2+1][y2+1] == '0':
                    q.append((x2, y2, x2+1, y2+1, 2))
        elif shape == 1 and x2 + 1 < n: # 세로
            if arr[x2+1][y2] == '0':
                q.append((x2, y2, x2+1, y2, 1))
                if y2 + 1 < n and arr[x2][y2+1] == '0' and arr[x2+1][y2+1] == '0':
                    q.append((x2, y2, x2+1, y2+1, 2))
        elif shape == 2: # 대각선
            if y2 + 1 < n and arr[x2][y2+1] == '0':
                q.append((x2, y2, x2, y2+1, 0))
            if x2 + 1 < n and arr[x2+1][y2] == '0':
                q.append((x2, y2, x2+1, y2, 1))
            if x2 + 1 < n and y2 + 1 < n and arr[x2][y2+1] == '0' and arr[x2+1][y2] == '0' and arr[x2+1][y2+1] == '0':
                q.append((x2, y2, x2+1, y2+1, 2))
    
    print(answer)

if __name__ == "__main__":
	main()