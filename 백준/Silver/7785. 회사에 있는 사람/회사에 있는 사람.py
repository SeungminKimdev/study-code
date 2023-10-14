import sys
input = sys.stdin.readline

def main():
    people = {}
    n = int(input())
    for _ in range(n):
        name, loc = input().split()
        if loc == 'enter':
            people[name] = True
        else:
            people[name] = False
    ans = []
    for i,j in people.items():
        if j:
            ans.append(i)
    ans.sort(reverse=True)
    print(*ans,sep='\n')

if __name__ == "__main__":
    main()