import sys
input = sys.stdin.readline

def main():
    case_num = 1
    while True:
        # 투표 수(ballots_count)와 후보 수(cand_count)를 읽음
        line = input().strip()
        if not line:
            break
        ballots_count, cand_count = map(int, line.split())
        if ballots_count == 0 and cand_count == 0:
            break

        # 각 투표의 순위 정보를 저장할 리스트 pos:
        # pos[k][i]는 k번째 투표에서 후보 i의 순위(0: 최고)를 의미함.
        pos = []
        for _ in range(ballots_count):
            ranking = list(map(int, input().split()))
            pos_ballot = [0] * cand_count
            for rank, candidate in enumerate(ranking):
                pos_ballot[candidate] = rank
            pos.append(pos_ballot)

        # 토너먼트 알고리즘을 이용하여 잠재적 콩도르세 승자 후보 찾기.
        candidate = 0
        for i in range(1, cand_count):
            wins = 0
            for k in range(ballots_count):
                if pos[k][i] < pos[k][candidate]:
                    wins += 1
            # 이긴 투표 수가 과반수를 초과하면 i가 후보가 됨.
            if wins > ballots_count // 2:
                candidate = i

        # 후보 candidate가 실제로 다른 모든 후보와 1:1 대결에서 승리하는지 검증.
        is_winner = True
        for j in range(cand_count):
            if j == candidate:
                continue
            wins = 0
            for k in range(ballots_count):
                if pos[k][candidate] < pos[k][j]:
                    wins += 1
            # 승리 조건: 상대 후보와 비교하여 이긴 투표 수가 전체의 과반수를 넘어야 함.
            if wins <= ballots_count // 2:
                is_winner = False
                break

        if is_winner:
            print(f"Case {case_num}: {candidate}")
        else:
            print(f"Case {case_num}: No Condorcet winner")
        case_num += 1

if __name__ == "__main__":
    main()