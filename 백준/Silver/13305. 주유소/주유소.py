import sys
input = sys.stdin.readline
MAX_INT = 1000000001

def main():
    n = int(input())
    dist = list(map(int,input().split()))
    price = list(map(int,input().split()))
    sumPrice = 0
    sumDis = 0
    lowPrice = MAX_INT
    for idx, nowPrice in enumerate(price[:-1]):
        if lowPrice < nowPrice:
            sumDis += dist[idx]
        else:
            sumPrice += lowPrice * sumDis
            lowPrice = nowPrice
            sumDis = dist[idx]
    sumPrice += lowPrice * sumDis
    print(sumPrice)
    return

if __name__ == '__main__':
    main()