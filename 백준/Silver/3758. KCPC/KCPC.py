import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        # 팀 수, 문제 수, 팀  ID, 로그 엔트리 수
        n, k, target_id, m = map(int, input().split())
        scores = [[0] * (k+1) for _ in range(n+1)]
        total_submission = [0] * (n+1)
        last_submission_time = [-1] * (n+1)
        for i in range(m):
            team_id, problem_j, score_s = map(int, input().split())
            scores[team_id][problem_j] = max(scores[team_id][problem_j], score_s)
            total_submission[team_id] += 1
            last_submission_time[team_id] = i
        total_scores = [(sum(scores[i]), total_submission[i], last_submission_time[i], i) for i in range(1, n+1)]
        total_scores.sort(key=lambda x: (-x[0], x[1], x[2]))
        for rank, team in enumerate(total_scores, start=1):
            if team[3] == target_id:
                print(rank)
                break
if __name__ == "__main__":
    main()