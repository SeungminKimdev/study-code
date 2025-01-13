import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        rank = list(map(int, input().split()))
        teams = {} # 팀인원 수
        scores = {}
        for team in rank:
            if team in teams:
                teams[team] += 1
            else:
                teams[team] = 1 
        # 점수합, 5등 위치, 점수 등록 인원
        scores = {team: [0, 0, 0] for team in teams.keys() if teams[team] == 6}
        
        score = 1
        for i, team in enumerate(rank):
            if team not in scores:
                continue
            if scores[team][2] < 4: # 4명까지만 점수 부여
                scores[team][0] += score
            scores[team][2] += 1
            if scores[team][2] == 5: # 5등 위치
                scores[team][1] = i
            score += 1
        
        result = sorted(scores.items(), key=lambda x: (x[1][0], x[1][1]))
        print(result[0][0])

if __name__ == "__main__":
	main()