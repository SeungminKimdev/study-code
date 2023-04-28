import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [int(i) for i in input().split()]
minT = 0
maxT = max(tree)
midT = maxT // 2

while minT + 1 < maxT:
    sum = 0
    for i in tree:
        if i > midT:
            sum += (i - midT)
        
    if sum >= m:
        minT = midT
    elif sum < m:
        maxT = midT
    midT = (minT + maxT) // 2
    
print(minT)