import sys
input = sys.stdin.readline

if __name__ == '__main__':
    s = input().rstrip()
    length = len(s)
    check = {}
    for i in range(length):
        for j in range(i+1,length+1):
            cut = s[i:j]
            if cut in check:
                continue
            else:
                check[cut] = True
    print(len(check.keys()))