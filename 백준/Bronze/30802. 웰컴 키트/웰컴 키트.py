import math

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

tShirt = 0
for i in size:
    tShirt += math.ceil(i/T)
print(tShirt)
print(f'{N // P} {N % P}')