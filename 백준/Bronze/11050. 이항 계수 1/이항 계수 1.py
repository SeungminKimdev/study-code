import sys
input = sys.stdin.readline

def facto(num):
    answer = 1
    for i in range(1,num+1):
        answer *= i
    return answer

a, b = map(int, input().split())
print(int((facto(a) / facto(a-b)) / facto(b)))