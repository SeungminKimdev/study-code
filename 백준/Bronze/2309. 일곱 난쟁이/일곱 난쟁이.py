import sys
input = sys.stdin.readline

def main():
    man = [int(input()) for _ in range(9)]
    man.sort()
    for i in range(8):
        for j in range(i+1, 9):
            if sum(man) - man[i] - man[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(man[k])
                return

if __name__ == "__main__":
    main()