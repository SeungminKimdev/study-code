import sys
input = sys.stdin.readline

def matrix_mul(a, b, m, n, p, q, case_num): # a[m][n] * b[p][q]
    print(f"Case #{case_num}:")
    if n != p:
        print("undefined")
        return
    c = [[0] * q for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    for i in range(m):
        print(f"| {' '.join(map(str, c[i]))} |")

def main():
    case_num = 1
    m, n, p, q = map(int, input().split())
    while m != 0 and n != 0 and p != 0 and q != 0:
        a = [list(map(int, input().split())) for _ in range(m)]
        b = [list(map(int, input().split())) for _ in range(p)]
        matrix_mul(a, b, m, n, p, q, case_num)
        m, n, p, q = map(int, input().split())
        case_num += 1

if __name__ == "__main__":
    main()