import sys
input = sys.stdin.readline

def main():
    totalTime = int(input())
    cook = [300,60,10]
    answer = []
    for i in cook:
        touch,totalTime = divmod(totalTime,i)
        answer.append(touch)
    if totalTime == 0:
        print(*answer,sep=' ')
    else:
        print('-1')
    return

if __name__ == '__main__':
    main()