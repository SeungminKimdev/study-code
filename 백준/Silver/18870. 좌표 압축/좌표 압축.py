import sys
input = sys.stdin.readline

def main():
    _ = int(input())
    inputNum = list(map(int,input().split()))
    setNum = sorted(set(inputNum))
    numList = {setNum[i]:i for i in range(len(setNum))}
    
    print(" ".join(str(numList[i]) for i in inputNum))

if __name__ == "__main__":
    main()