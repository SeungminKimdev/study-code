A, B = map(int,input().split())
time = int(input())

A += (B + time) // 60
if A >= 24:
    A = A - 24
B = (B + time) % 60
print('%d %d'%(A,B))