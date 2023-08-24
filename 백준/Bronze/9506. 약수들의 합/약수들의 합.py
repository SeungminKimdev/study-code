import sys
input = sys.stdin.readline

def main():
    num = int(input())
    while num != -1:
        check = []
        for i in range(1,num):
            if num % i == 0:
                check.append(i)
        if sum(check) == num:
            print(num,' = ',' + '.join(str(i) for i in check), sep = '')
        else:
            print(str(num) + ' is NOT perfect.')
        num = int(input())

if __name__ == "__main__":
    main()