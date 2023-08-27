import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    if n == 1:
        print(0)
        print(1)
        return
    
    count = [0]*(n+1)
    root = {}
    q = deque([1])
    root[1] = [1]
    while q:
        num = q.popleft()
        num3 = num*3
        if num3 <= n and (count[num3] == 0 or (count[num3] != 0 and count[num3] > count[num] + 1)):
            count[num3] = count[num] + 1
            root[num3] = root[num] + [num3]
            q.append(num3)
        num2 = num*2
        if num2 <= n and (count[num2] == 0 or (count[num2] != 0 and count[num2] > count[num] + 1)):
            count[num2] = count[num] + 1
            root[num2] = root[num] + [num2]
            q.append(num2)
        num1 = num+1
        if num1 <= n and (count[num1] == 0 or (count[num1] != 0 and count[num1] > count[num] + 1)):
            count[num1] = count[num] + 1
            root[num1] = root[num] + [num1]
            q.append(num1)
            
    print(count[n])
    print(*reversed(root[n]))

if __name__ == "__main__":
    main()