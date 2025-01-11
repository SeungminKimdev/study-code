import sys
input = sys.stdin.readline

def main():
    n, inputScore, p = map(int, input().split())
    if n == 0:
        print(1)
        return
    
    scores = list(map(int, input().split()))
    
    rank = 1
    for score in scores:
        if inputScore < score:
            rank += 1
        else:
            break
    
    if (n == p and inputScore <= scores[-1]) or rank > p:
        print(-1)
    else:
        print(rank)

if __name__ == "__main__":
	main()