import sys
input = sys.stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        money = int(input())
        answer =  []
        coin, money = divmod(money,25)
        answer.append(coin)
        coin, money = divmod(money,10)
        answer.append(coin)
        coin, money = divmod(money,5)
        answer.append(coin)
        answer.append(money)
        print(*answer,sep=" ")
    return

if __name__ == '__main__':
    main()