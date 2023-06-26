import sys
input = sys.stdin.readline

def main():
    grade = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
    sum = 0
    gSum = 0
    for _ in range(20):
        _, p, g = input().split()
        if g == 'P':
            continue
        else:
            sum += float(p) * grade[g]
            gSum += float(p)
    if gSum == 0:
        print(0)
    else:
        print(sum/gSum)

if __name__ == "__main__":
    main()