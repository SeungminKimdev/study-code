import sys
input = sys.stdin.readline
import heapq
def main():
    n = int(input())
    A = list(map(int,input().split()))
    heapq.heapify(A)
    B = list(map(int,input().split()))
    B1 = [-i for i in B]
    heapq.heapify(B1)
    sum = 0
    for _ in range(n):
        sum += heapq.heappop(A) * -heapq.heappop(B1)
    print(sum)
    return

if __name__ == '__main__':
    main()