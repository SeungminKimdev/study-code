import sys
input = sys.stdin.readline

def countDis(a, b, c):
    ans = 0
    for i in range(4):
        if a[i] not in b:
            ans += 1
        if a[i] not in c:
            ans += 1
        if b[i] not in c:
            ans += 1
    return ans

def main():
    n = int(input())
    for _ in range(n):
        num = int(input())
        people = list(input().split())
        ans = 12
        if num < 33:
            for i in range(num-2):
                for j in range(i+1,num-1):
                    for k in range(j+1,num):
                        ans = min(ans,countDis(people[i],people[j],people[k]))
        else:
            ans = 0
        print(ans)
    return

if __name__ == '__main__':
    main()