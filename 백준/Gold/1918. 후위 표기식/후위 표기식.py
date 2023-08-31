import sys
input = sys.stdin.readline
from collections import deque

def solution():
    s = input().rstrip()
    dq = deque()
    answer = ''
    length = len(s)
    for i in range(length):
        if s[i] == '(':
            dq.append(s[i])
        elif s[i] == ')':
            while dq:
                tempPop = dq.pop()
                if tempPop == '(':
                    break
                answer += tempPop
        elif s[i] == '+' or s[i] == '-':
            while dq:
                tempPop = dq.pop()
                if tempPop == '(':
                    dq.append(tempPop)
                    break
                answer += tempPop
            dq.append(s[i])
        elif s[i] == '*' or s[i] == '/':
            if len(dq) != 0:
                if dq[-1] == '*' or dq[-1] == '/':
                    answer += dq.pop()
            dq.append(s[i])
        else:
            answer += s[i]
    while dq:
        answer += dq.pop()
    print(answer)

if __name__ == '__main__':
    solution()