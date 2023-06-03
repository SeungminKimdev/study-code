import sys
input = sys.stdin.readline

def main():
    inputNum = [int(input()) for _ in range(3)]
    if sum(inputNum) != 180:
        return print('Error')
    inputSet = set(inputNum)
    if len(inputSet) == 1:
        return print('Equilateral')
    elif len(inputSet) == 2:
        return print('Isosceles')
    else:
        return print('Scalene')
    
if __name__ == '__main__':
    main()