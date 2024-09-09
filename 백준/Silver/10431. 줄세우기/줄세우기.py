n = int(input())

for _ in range(n):
    height = list(map(int,input().split()))
    walking = 0
    sorted_height = []
    for i in range(1,len(height)):
        if sorted_height:
            for check in range(i-1):
                if sorted_height[check] > height[i]:
                    sorted_height = sorted_height[:check] + [height[i]] + sorted_height[check:]
                    walking += (i-1-check)
                    break
                if check == (i-2):
                    sorted_height.append(height[i])
        else:
            sorted_height.append(height[i])
    
    print(f'{height[0]} {walking}')