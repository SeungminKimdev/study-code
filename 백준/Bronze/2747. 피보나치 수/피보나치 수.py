import sys
input = sys.stdin.readline

def main():
    n = int(input())
    fb = [0, 1]
    for i in range(2, n+1):
        fb.append(fb[i-1] + fb[i-2])
    print(fb[n])

if __name__ == "__main__":
    main()