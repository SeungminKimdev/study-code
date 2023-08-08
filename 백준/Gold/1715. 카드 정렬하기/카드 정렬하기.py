import sys
input = sys.stdin.readline
from queue import PriorityQueue
def main():
    q = PriorityQueue()
    n = int(input())
    for _ in range(n):
        temp = int(input())
        q.put(temp)
    ans = 0
    for _ in range(n-1):
        temp = q.get() + q.get()
        ans += temp
        q.put(temp)
    print(ans)
    return

if __name__ == '__main__':
    main()