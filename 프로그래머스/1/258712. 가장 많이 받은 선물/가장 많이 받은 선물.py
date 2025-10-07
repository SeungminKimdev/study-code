# 선물지수 = 준 선물 - 받은 선물 (선물 지수가 큰 사람 <- 작은 사람)
# gifts : A -> B

def solution(friends, gifts):
    gift_scores = {friend:0 for friend in friends}
    gift_record = {giver:{getter:0 for getter in friends} for giver in friends}
    gift_current = {friend:0 for friend in friends}
    
    for gift in gifts:
        giver, getter = gift.split(' ')
        gift_record[giver][getter] += 1
        gift_scores[giver] += 1
        gift_scores[getter] -= 1

    friends_num = len(friends)
    for a in range(friends_num-1):
        for b in range(a+1, friends_num):
            friend_a = friends[a]
            friend_b = friends[b]
            if gift_record[friend_a][friend_b] > gift_record[friend_b][friend_a]:
                gift_current[friend_a] += 1
            elif gift_record[friend_a][friend_b] < gift_record[friend_b][friend_a]:
                gift_current[friend_b] += 1
            else:
                if gift_scores[friend_a] > gift_scores[friend_b]:
                    gift_current[friend_a] += 1
                elif gift_scores[friend_a] < gift_scores[friend_b]:
                    gift_current[friend_b] += 1
                else:
                    continue
    
    return max(gift_current.values())