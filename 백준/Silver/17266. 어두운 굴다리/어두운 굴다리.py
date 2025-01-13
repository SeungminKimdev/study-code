import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())
    x = list(map(int, input().split()))
    ansList = [x[0], N-x[-1], 0] # 시작부터 가로등까지, 끝부터 가로등까지, 중간 가로등사이 거리 최대
    for i in range(0, M-1):
        ansList[2] = max(ansList[2], sum(divmod((x[i+1]-x[i]),2)))
    print(max(ansList))

if __name__ == "__main__":
	main()