import sys
input = sys.stdin.readline

def main():
    n = int(input())
    numList = dict()
    inputNum = list(map(int,input().split()))
    
    setNum = sorted(set(inputNum))
    for i in range(len(setNum)):
        numList[setNum[i]] = i
    ans = ""
    for i in inputNum:
        ans += str(numList[i])
        ans += " "
    print(ans.rstrip())

if __name__ == "__main__":
    main()