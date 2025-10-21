import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    table = list(input().strip())
    table_length = len(table)
    answer = 0
    
    for i in range(table_length):
        if table[i] == 'P':
            for j in range(max(0, i-K), min(table_length, i+K+1)):
                if table[j] == 'H':
                    table[j] = 'X'
                    answer += 1
                    break
    
    print(answer)
    return

if __name__ == "__main__":
    main()