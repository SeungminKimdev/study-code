n = int(input())
numList = list(input().split())
answer = 0
left = 0
check = {}

for right in range(n):
    if numList[right] in check:
        check[numList[right]] += 1
    else:
        check[numList[right]] = 1

    while len(check) > 2:
        check[numList[left]] -= 1
        if check[numList[left]] == 0:
            del check[numList[left]]
        left += 1

    answer = max(answer, right - left + 1)

print(answer)