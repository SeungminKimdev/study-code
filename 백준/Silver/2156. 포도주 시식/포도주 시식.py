import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(int(input()))
    else:
        arr = [int(input()) for _ in range(n)]
        grape = [0,arr[0],arr[1]+arr[0]]
        for i in range(2,n):
            grape.append(max(grape[i],max(grape[i-1]+arr[i],grape[i-2]+arr[i]+arr[i-1])))
        print(grape[n])