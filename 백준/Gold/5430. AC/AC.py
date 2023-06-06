import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    for _ in range(n):
        command = input().strip()
        commandLen = len(command)
        numLen = int(input())
        if numLen == 0:
            _ = input()
            numList = deque()
        else:
            numList = deque(input().strip().lstrip('[').rstrip(']').split(','))
        reverse = False
        ans = ''
        for i in range(commandLen):
            if command[i] == 'R':
                reverse = not reverse
            else:
                if numLen == 0:
                    ans = 'error'
                    break
                if reverse:
                    numList.pop()
                else:
                    numList.popleft()
                numLen -= 1
        
        if ans != 'error':
            ans = '['
            if reverse:
                for _ in range(numLen):
                    ans += numList.pop()
                    ans += ','
            else:
                for _ in range(numLen):
                    ans += numList.popleft()
                    ans += ','
            ans = ans.rstrip(',')
            ans += ']'
        print(ans)
    return

if __name__ == '__main__':
    main()