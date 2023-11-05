import sys
input = sys.stdin.readline

def main():
    n = int(input())
    scT = []
    scP = []
    for _ in range(n):
        t,p = map(int,input().split())
        scT.append(t)
        scP.append(p)
    dp =  [0 for _ in range(n+1)]
    for i in range(n):
        for j in range(i+scT[i],n+1):
            dp[j] = max(dp[j],dp[i] + scP[i])
    print(dp[-1])
    
if __name__ == "__main__":
    main()