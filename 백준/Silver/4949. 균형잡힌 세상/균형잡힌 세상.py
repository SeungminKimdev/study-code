import sys
input = sys.stdin.readline
from collections import deque

line = input()
while line != ".\n":
    check = deque()
    answer = "yes"
    for i in line:
        if i == '(' or i =='[' or i == '{':
            check.append(i)
        elif i == ')':
            if len(check) == 0 or check.pop() != '(':
                answer = "no"
                break
        elif i == ']':
            if len(check) == 0 or check.pop() != '[':
                answer = "no"
                break
        elif i == '}':
            if len(check == 0) or check.pop() != '{':
                answer = "no"
                break
    if len(check) != 0:
        answer = "no"
    print(answer)
    line = input()