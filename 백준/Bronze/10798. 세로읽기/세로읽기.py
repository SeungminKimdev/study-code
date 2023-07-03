import sys
input = sys.stdin.readline

def main():
    inputS = []
    length = []
    for _ in range(5):
        inS = input().rstrip()
        inputS.append(inS)
        length.append(len(inS))
    answer = ""
    for i in range(max(length)):
        for j in range(5):
            if i < length[j]:
                answer += inputS[j][i]
            
    print(answer)

if __name__ == "__main__":
    main()