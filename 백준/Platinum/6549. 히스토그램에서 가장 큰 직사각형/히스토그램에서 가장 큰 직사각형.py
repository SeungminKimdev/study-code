import sys
input = sys.stdin.readline

def main():
    while True:
        testCase = list(map(int,input().split()))
        if testCase == [0]:
            break
        
        stack = []
        ans = 0
        for i, high in enumerate(testCase):
            if i == 0:
                continue
            if stack and stack[-1][1] > high:
                while stack:
                    _, tempH = stack.pop()
                    width = 1
                    if stack:
                        width = stack[-1][0] + 1
                    tempS = (i-width) * tempH
                    ans = max(ans,tempS)
                    if not stack or stack[-1][1] <= high:
                        break
            if not stack or stack[-1][1] <= high:
                stack.append((i,high))
        
        while stack:
            _, tempH = stack.pop()
            width = 1
            if stack:
                width = stack[-1][0] + 1
            tempS = (testCase[0] + 1 - width) * tempH
            ans = max(ans,tempS)

        print(ans)

if __name__ == '__main__':
    main()