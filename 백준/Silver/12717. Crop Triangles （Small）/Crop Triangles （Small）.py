import sys
input = sys.stdin.readline

def main():
    test_case = int(input())
    for case_num in range(test_case):
        n, A, B, C, D, x, y, M = map(int, input().split())
        trees = []
        trees.append((x, y))
        for _ in range(n-1):
            x = (A * x + B) % M
            y = (C * y + D) % M
            trees.append((x, y))
        answer = 0
        for i in range(n):
            x1, y1 = trees[i]
            for j in range(i+1, n):
                x2, y2 = trees[j]
                for k in range(j+1, n):
                    x3, y3 = trees[k]
                    if (x1 + x2 + x3) % 3 == 0 and (y1 + y2 + y3) % 3 == 0:
                        answer += 1
        print(f"Case #{case_num+1}: {answer}")

if __name__ == "__main__":
    main()