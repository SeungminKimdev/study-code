import sys
input = sys.stdin.readline

def main():
    n = int(input())
    number = input().rstrip()
    evens = ['0', '2', '4', '6', '8'] # 짝수
    
    even = odd = 0
    for i in range(n):
        if number[i] in evens:
            even += 1
        else:
            odd += 1
    
    if even > odd:
        print(0)
    elif even < odd:
        print(1)
    else:
        print(-1)

if __name__ == "__main__":
    main()