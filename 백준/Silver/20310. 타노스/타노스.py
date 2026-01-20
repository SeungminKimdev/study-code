import sys
input = sys.stdin.readline

def main():
    s = list(input().rstrip())
    length = len(s)
    zeros = s.count('0') // 2
    for i in range(length-1, -1, -1):
        if s[i] == '0' and zeros > 0:
            s[i] = 'x'
            zeros -= 1
        if zeros == 0:
            break
    ones = s.count('1') // 2
    for i in range(0, length, 1):
        if s[i] == '1' and ones > 0:
            s[i] = 'x'
            ones -= 1
        if ones == 0:
            break
    answer = ''.join([n for n in s if n != 'x'])
    print(answer)

if __name__ == "__main__":
    main()