import bisect
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    lis = []
    
    for num in arr:
        pos = bisect.bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    
    print(len(lis))

if __name__ == "__main__":
	main()