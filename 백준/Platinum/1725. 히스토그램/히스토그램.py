import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n == 1:
        return print(int(input()))
    testCase = []
    for _ in range(n):
        testCase.append(int(input()))
    stack = []
    ans = 0
    for i, high in enumerate(testCase):
        if stack and stack[-1][1] > high:
            while stack:
                _, tempH = stack.pop()
                width = 1
                if stack:
                    width = stack[-1][0] + 1
                tempS = (i+1-width) * tempH
                ans = max(ans,tempS)
                if not stack or stack[-1][1] <= high:
                    break
        if not stack or stack[-1][1] <= high:
            stack.append((i+1,high))

    while stack:
        _, tempH = stack.pop()
        width = 1
        if stack:
            width = stack[-1][0] + 1
        tempS = (n + 1 - width) * tempH
        ans = max(ans,tempS)
    print(ans)

if __name__ == '__main__':
    main()