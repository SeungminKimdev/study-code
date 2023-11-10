import sys
input = sys.stdin.readline

def main():
    n = int(input())
    result = 0
    x = 1
    while x*x <= n:
        x += 1
        result +=1
    print(result)
    
if __name__ == "__main__":
    main()