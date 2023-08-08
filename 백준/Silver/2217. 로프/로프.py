import sys
input = sys.stdin.readline

def main():
    n = int(input())
    rope = []
    for _ in range(n):
        tempIn = int(input())
        rope.append(tempIn)
    rope.sort(reverse=True)
    for i in range(n):
        rope[i] *= (i+1)
    print(max(rope))
    return

if __name__ == '__main__':
    main()