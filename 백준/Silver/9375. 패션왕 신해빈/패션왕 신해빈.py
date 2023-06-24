import sys
input = sys.stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        wear = {}
        m = int(input())
        for _ in range(m):
            close, tag = input().split()
            if tag in wear:
                wear[tag].append(close)
            else:
                wear[tag] = [close]
        answer = 1
        for i in wear.keys():
            answer *= (len(wear[i]) + 1)
        print(answer - 1)
    return

if __name__ == '__main__':
    main()