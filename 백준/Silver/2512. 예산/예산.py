import sys
input = sys.stdin.readline

def main():
    n = int(input())
    prices = list(map(int, input().split()))
    max_price = int(input())
    
    if sum(prices) <= max_price:
        print(max(prices))
        return
    
    prices.sort()
    for price in prices:
        if price * n < max_price:
            n -= 1
            if n == 0:
                print(price)
                return
            max_price -= price
        elif price * n == max_price:
            print(price)
            return
        else:
            print(max_price // n)
            return
    return

if __name__ == "__main__":
    main()