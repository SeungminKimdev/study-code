import sys
input = sys.stdin.readline

def coin():
    coinList = []
    n, k = map(int,input().split())
    for _ in range(n):
        coinList.append(int(input()))
    coinSum = 0
    coinList = reversed(coinList)
    for i in coinList:
        temp = k // i
        coinSum += temp
        k -= i * temp
    return print(coinSum)

if __name__ == "__main__":
    coin()