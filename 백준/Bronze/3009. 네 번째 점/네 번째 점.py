import sys
input = sys.stdin.readline

def main():
    x = {}
    y = {}
    for _ in range(3):
        a,b = map(int,input().split())
        if a not in x:
            x[a] = 1
        else:
            x[a] += 1
        if b not in y:
            y[b] = 1
        else:
            y[b] += 1
    answer = [0,0]
    for i in x.keys():
        if x[i] == 1:
            answer[0] = i
    for i in y.keys():
        if y[i] == 1:
            answer[1] = i
    print(*answer,sep=" ")
    return

if __name__ == '__main__':
    main()