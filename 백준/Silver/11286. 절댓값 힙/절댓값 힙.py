import sys
input = sys.stdin.readline
import heapq

def main():
    n = int(input())
    plusq = []
    minusq = []
    
    for _ in range(n):
        inputNum = int(input())
        if inputNum == 0:
            if len(plusq) == 0 and len(minusq) == 0:
                print('0')
            elif len(plusq) == 0:
                print(-heapq.heappop(minusq))
            elif len(minusq) == 0:
                print(heapq.heappop(plusq))
            else:
                if plusq[0] == minusq[0]:
                    print(-heapq.heappop(minusq))
                elif plusq[0] > minusq[0]:
                    print(-heapq.heappop(minusq))
                else:
                    print(heapq.heappop(plusq))
        elif inputNum > 0:
            heapq.heappush(plusq,inputNum)
        else:
            heapq.heappush(minusq,-inputNum)

if __name__ == '__main__':
    main()