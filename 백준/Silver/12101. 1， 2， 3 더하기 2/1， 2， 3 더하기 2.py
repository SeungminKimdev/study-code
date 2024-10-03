import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    numbers = []
    
    def dfs(nums):
        if sum(nums) == n:
            numbers.append(nums)
        if len(nums) > n:
            return
        for i in range(1,4):
            dfs(nums + [i])
    dfs([])
    if len(numbers) < k:
        print('-1')
    else:
        print('+'.join(map(str, numbers[k-1])))
    return

if __name__ == "__main__":
    main()