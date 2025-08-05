import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()
    s_len = len(s)
    weight = [1, 3]
    ISBN = 0
    
    for i in range(s_len):
        if s[i] == '*':
            check_weight = weight[i % 2]
            continue
        ISBN += int(s[i]) * weight[i % 2]
        ISBN %= 10
    
    for i in range(10):
        if (ISBN + i * check_weight) % 10 == 0:
            print(i)
            break
    return

if __name__ == "__main__":
    main()