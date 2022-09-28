remain = {}
for i in range(10):
    N = int(input())
    N = N % 42
    try:
        remain[N] += 1
    except:
        remain[N] = 1

print(len(remain.keys()))