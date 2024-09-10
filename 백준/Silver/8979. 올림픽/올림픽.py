import sys
input = sys.stdin.readline

N, K = map(int, input().split())

medals = []
for _ in range(N):
    medal = list(map(int, input().split()))
    if medal[0] == K:
        targetMedals = medal
    medals.append(medal)
rank = 1
for i in range(N):
    if medals[i][1] > targetMedals[1]:
        rank += 1
    elif medals[i][1] == targetMedals[1]:
        if medals[i][2] > targetMedals[2]:
            rank += 1
        elif medals[i][2] == targetMedals[2]:
            if medals[i][3] > targetMedals[3]:
                rank += 1
print(rank)