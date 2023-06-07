import sys
input = sys.stdin.readline
from collections import deque

def main():
    n = int(input())
    for _ in range(n):
        A, B = map(int,input().split())
        visited = [False] * 10001
        dq = deque()
        dq.append((A,''))
        
        while dq:
            num, command = dq.popleft()
            visited[num] = True
            if num == B:
                print(command)
                break
            
            temp = (2 * num) % 10000
            if not visited[temp]:
                dq.append((temp,command+'D'))
                visited[temp] = True
                
            temp = (num-1) % 10000
            if not visited[temp]:
                dq.append((temp,command+'S'))
                visited[temp] = True
            
            temp = (10*num+(num//1000))%10000
            if not visited[temp]:
                dq.append((temp,command+'L'))
                visited[temp] = True
                
            temp = (num//10+(num%10)*1000)%10000
            if not visited[temp]:
                dq.append((temp,command+'R'))
                visited[temp] = True
    return

if __name__ == '__main__':
    main()