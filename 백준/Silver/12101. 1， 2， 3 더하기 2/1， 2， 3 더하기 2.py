import sys
input = sys.stdin.readline

def dfs(nums, n, numbers):
    sumNums = sum(nums)
    if sumNums == n:
        numbers.append(nums)
    elif sumNums > n:
        return
    if len(nums) > n:
        return
    for i in range(1, 4):
        dfs(nums + [i], n, numbers)

def main():
    n, k = map(int, input().split())
    numbers = []
    dfs([], n, numbers)
    if len(numbers) < k:
        print('-1')
    else:
        print('+'.join(map(str, numbers[k-1])))
    return

if __name__ == "__main__":
    main()