def solution(players, callings):
    n = len(players)
    answer = players #rank:name
    rankRname = {players[i]:i for i in range(n)} #name:rank
    for i in callings:
        now = rankRname[i]
        rankRname[i] -= 1
        rankRname[answer[now-1]] += 1
        answer[now], answer[now-1] = answer[now-1], answer[now]
    return answer