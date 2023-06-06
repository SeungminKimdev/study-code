import sys
input = sys.stdin.readline

def new_round(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)

def main():
    n = int(input())
    if n == 0:
        return print('0')
    
    opinion = [int(input()) for _ in range(n)]
    opinion.sort()
    cutN = new_round(n * 0.15)
    return print(new_round(sum(opinion[cutN:n-cutN]) / (n - 2*cutN)))

if __name__ == '__main__':
    main()