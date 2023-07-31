import sys
input = sys.stdin.readline

def checkDis(x,y,cx,cy,r):
    if r**2 > (x-cx)**2 + (y-cy)**2:
        return True
    else:
        return False

def main():
    t = int(input())
    for _ in range(t):
        x1, y1, x2, y2 = map(int,input().split())
        n = int(input())
        ans = 0
        for _ in range(n):
            cx, cy, r = map(int,input().split())
            if checkDis(x1,y1,cx,cy,r) != checkDis(x2,y2,cx,cy,r):
                ans += 1
        print(ans)
    return

if __name__ == '__main__':
    main()