def solution(food):
    front = ''
    foodLen = len(food)
    for i in range(1,foodLen):
        front += str(i)*(food[i]//2)
    answer = front + '0' + front[::-1]
    return answer