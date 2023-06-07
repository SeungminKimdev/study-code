import sys
input = sys.stdin.readline

def main():
    money = 1000 - int(input())
    coin = [500,100,50,10,5,1]
    sum = 0
    for i in coin:
        temp = money // i
        sum += temp
        money -= temp * i
    print(sum)
    return

if __name__ == '__main__':
    main()