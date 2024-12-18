import sys
input = sys.stdin.readline

def main():
    w, h = map(int, input().split())
    p, q = map(int, input().split())
    t = int(input())

    if ((p + t) // w) % 2 == 0:
        p = (p + t) % w
    else:
        p = w - (p + t) % w
    if ((q + t) // h) % 2 == 0:
        q = (q + t) % h
    else:
        q = h - (q + t) % h
    print(f"{p} {q}")

if __name__ == "__main__":
	main()