import sys
input = sys.stdin.readline

def main():
    N, game = input().split()
    N = int(N)
    userList = set()
    for _ in range(N):
        userList.add(input())
    if game == 'Y':
        print(len(userList) // 1)
    elif game == 'F':
        print(len(userList) // 2)
    elif game == 'O':
        print(len(userList) // 3)
    else:
        return

if __name__ == "__main__":
    main()