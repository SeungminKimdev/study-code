import sys
input = sys.stdin.readline

def main():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    M = int(input().strip())
    B = list(map(int, input().strip().split()))
    answer = []
    
    idx_a = 0
    idx_b = 0

    while True:
        found = False
        for num in range(100, 0, -1):
            temp_a = -1
            for a in range(idx_a, N):
                if A[a] == num:
                    temp_a = a
                    break
                    
            temp_b = -1
            for b in range(idx_b, M):
                if B[b] == num:
                    temp_b = b
                    break
                    
            if temp_a != -1 and temp_b != -1:
                answer.append(num)
                idx_a = temp_a + 1
                idx_b = temp_b + 1
                found = True
                break
        if not found:
            break
    
    if len(answer) > 0:
        print(len(answer))
        print(*answer)
    else:
        print(0)
    return

if __name__ == "__main__":
    main()