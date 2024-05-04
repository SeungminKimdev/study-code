def solution(bridge_length, weight, truck_weights):
    answer = 1
    i = 1
    weight_sum = truck_weights[0]
    bridge = [0]*(bridge_length-1) + [truck_weights[0]]
    while i < len(truck_weights):
        answer += 1
        weight_sum -= bridge.pop(0)
        if i >= len(truck_weights) or weight_sum + truck_weights[i] > weight:
            bridge.append(0)
        else:
            bridge.append(truck_weights[i])
            weight_sum += truck_weights[i]
            i += 1
    answer += bridge_length
    return answer