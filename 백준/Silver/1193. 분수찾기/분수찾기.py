import sys
input = sys.stdin.readline

def main():
    n = int(input())
    line = 1 
    while n > line:
        n -= line
        line += 1
    
    if line % 2 == 0:
        n1 = n
        n2 = line - n + 1
    else:
        n1 = line - n + 1
        n2 = n
    print(str(n1)+'/'+str(n2))

if __name__ == "__main__":
    main()