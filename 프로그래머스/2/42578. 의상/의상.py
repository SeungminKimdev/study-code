def solution(clothes):
    closet = {}
    for cloth_name, cloth_value in clothes:
        if cloth_value not in closet:
            closet[cloth_value] = [cloth_name]
        else:
            closet[cloth_value].append(cloth_name)
    
    answer = 1
    for cloth_value in closet.keys():
        answer *= len(closet[cloth_value]) + 1
    return answer - 1