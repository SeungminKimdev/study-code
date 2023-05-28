import sys
input = sys.stdin.readline
import heapq

def main():
    n =  int(input())
    for _ in range(n):
        m = int(input())
        minQ = []
        maxQ = []
        numDic = {}
        len = 0
        for _ in range(m):
            command, num = input().split()
            if command == 'I':
                num = int(num)
                heapq.heappush(minQ,num) #오름차순
                heapq.heappush(maxQ,-num) #내림차순
                if num in numDic:
                    numDic[num] += 1
                else:
                    numDic[num] = 1
                len += 1
            elif command == 'D' and len != 0:
                if num == '1':
                    outNum = -heapq.heappop(maxQ)
                    while numDic[outNum] == 0:
                        outNum = -heapq.heappop(maxQ)
                    numDic[outNum] -= 1
                elif num == '-1':
                    outNum = heapq.heappop(minQ)
                    while numDic[outNum] == 0:
                        outNum = heapq.heappop(minQ)
                    numDic[outNum] -= 1
                len -= 1
        #출력
        if len == 0:
            print('EMPTY')
        else:
            outNum = -maxQ[0]
            while numDic[outNum] == 0:
                heapq.heappop(maxQ)
                outNum = -maxQ[0]
            outNum = minQ[0]
            while numDic[outNum] == 0:
                heapq.heappop(minQ)
                outNum = minQ[0]
            print(str(-maxQ[0]) + " " + str(minQ[0]))
    return

if __name__ == '__main__':
    main()