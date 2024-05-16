def solution(n, times):
    def binarySearch():
        l = 1
        r = min(times) * n + 1
        minT = r
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                r = mid - 1
                minT = mid
            else:
                l = mid + 1
        return minT
    
    def check(num):
        temp = 0
        for time in times:
            temp += num // time
            if temp > n:
                break
        if temp >= n:
            return True
        else:
            return False

    answer = binarySearch()
    return answer