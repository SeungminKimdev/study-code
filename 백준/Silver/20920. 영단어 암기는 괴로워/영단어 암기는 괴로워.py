import sys
from collections import Counter
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    letters = []
    for _ in range(n):
        letter = input().strip()
        if len(letter) < m:
            continue
        letters.append(letter)
    counter = Counter(letters)
    sorted_items = sorted(counter.items(), key=lambda x: (-x[1], -len(x[0]) ,x[0]))
    for letter, _ in sorted_items:
        print(letter)
    return

if __name__ == "__main__":
    main()