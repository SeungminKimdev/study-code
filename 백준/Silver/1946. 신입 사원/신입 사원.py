import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    for _ in range(n):
        participant = []
        people = int(input())
        for _ in range(people):
            a,b = map(int,input().split())
            participant.append((a,b))
        participant.sort()
        ans = 1
        check = participant[0][1]
        for i in range(1,people):
            if check > participant[i][1]:
                check = participant[i][1]
                ans += 1
        print(ans)

if __name__ == '__main__':
    solution()