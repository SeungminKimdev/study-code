import sys
input = sys.stdin.readline

def main():
    inputS = input().rstrip()
    rInputS = inputS[::-1]
    if inputS == rInputS:
        print('1')
    else:
        print('0')

if __name__ == "__main__":
    main()