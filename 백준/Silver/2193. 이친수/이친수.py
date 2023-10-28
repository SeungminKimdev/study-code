import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    two = [0,1]
    for i in range(1,n):
        two.append(two[-1]+two[-2])
    print(two[n])