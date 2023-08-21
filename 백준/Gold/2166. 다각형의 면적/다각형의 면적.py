import sys
input = sys.stdin.readline

def ccw(x1,x2,x3,y1,y2,y3):
    temp = x1*y2+x2*y3+x3*y1
    temp += (-y1*x2-y2*x3-y3*x1)
    return temp/2

def solution():
    n = int(input())
    point = []
    for _ in range(n):
        point.append(list(map(int,input().split())))
    ans = 0
    for i in range(2,n):
        ans += ccw(point[0][0],point[i-1][0],point[i][0],point[0][1],point[i-1][1],point[i][1])
    print(abs(ans))
if __name__ == '__main__':
    solution()