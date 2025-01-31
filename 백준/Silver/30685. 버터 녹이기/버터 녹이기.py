import sys
input = sys.stdin.readline

def max_safe_time(n, arr):
    arr.sort()  # 위치 기준 정렬

    # 버터가 완전히 퍼질 수 있는 최대 시간은 각 h에 대해 (h // 2)까지
    left, right = 0, max(h // 2 for _, h in arr)
    max_time = 0

    while left <= right:
        mid = (left + right) // 2
        merged = False

        # 첫 번째 버터의 확장 범위
        expand = min(arr[0][1] // 2, mid)
        prev_L, prev_R = arr[0][0] - expand, arr[0][0] + expand

        # 나머지 버터들도 mid초 동안 확장했을 때 겹치는지 확인
        for x, h in arr[1:]:
            expand = min(h // 2, mid)
            L, R = x - expand, x + expand
            if prev_R >= L:   # 겹친 경우
                merged = True
                break
            prev_L, prev_R = L, R

        if merged:
            right = mid - 1  # 겹쳤다면 시간을 줄여봄
        else:
            max_time = mid   # 겹치지 않으면 갱신
            left = mid + 1

    return max_time

def main():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    max_time = max_safe_time(n, arr)
    # 버터가 완전히 퍼질 수 있는 최대치
    full_expand_time = max(h // 2 for _, h in arr)

    # 만약 최대 가능한 확장 시간까지 겹치지 않는다면 그 이후로는 버터가 더 퍼지지 않으므로 영원히 가능
    if max_time == full_expand_time:
        print("forever")
    else:
        print(max_time)

if __name__ == "__main__":
    main()