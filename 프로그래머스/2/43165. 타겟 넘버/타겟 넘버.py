def solution(numbers, target):
    global answer
    answer = 0
    def dfs(floor, num):
        global answer
        if floor == len(numbers):
            if num == target:
                answer += 1
            return
        dfs(floor+1,num+numbers[floor])
        dfs(floor+1,num-numbers[floor])
        return
    dfs(0,0)
    return answer