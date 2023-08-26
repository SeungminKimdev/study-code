import sys
input = sys.stdin.readline

def main():
    num = input().rstrip()
    number = {i:0 for i in range(10)}
    for i in num:
        number[int(i)] += 1
    ans = ''
    for i in range(9,-1,-1):
        if number[i] != 0:
            ans += str(i) * number[i]
    print(ans)

if __name__ == "__main__":
    main()