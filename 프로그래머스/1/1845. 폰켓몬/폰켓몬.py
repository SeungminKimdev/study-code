def solution(nums):
    pocketmon_num = len(nums)
    answer = min(len(set(nums)), pocketmon_num // 2)
    return answer