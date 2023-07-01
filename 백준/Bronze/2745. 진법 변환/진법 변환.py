import sys
input = sys.stdin.readline

def main():
    number, B = input().split()
    B = int(B)
    print(int(number,B))

if __name__ == "__main__":
    main()