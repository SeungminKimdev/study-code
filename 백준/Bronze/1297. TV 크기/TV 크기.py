import sys
input = sys.stdin.readline

def main():
    d, h, w = map(int,input().split())
    d *= d
    h *= h
    w *= w
    x = d * w / (h+w)
    x = int(x**(1/2))
    y = d * h / (h+w)
    y = int(y**(1/2))
    print(str(y) + ' ' + str(x))
    return

if __name__ == '__main__':
    main()