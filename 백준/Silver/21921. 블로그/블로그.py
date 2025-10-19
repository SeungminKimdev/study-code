import sys
input = sys.stdin.readline

def main():
    N, X = map(int, input().split())
    visited = list(map(int, input().split()))
    
    max_visit = sum(visited[:X])
    max_visit_num = 1
    before_visit = max_visit
    
    for i in range(1, N-X+1):
        current_visit = before_visit - visited[i-1] + visited[i+X-1]
        before_visit = current_visit
        if current_visit > max_visit:
            max_visit = current_visit
            max_visit_num = 1
        elif current_visit == max_visit:
            max_visit_num += 1
        else:
            continue
        
    if max_visit == 0:
        print("SAD")
    else:
        print(max_visit)
        print(max_visit_num)
    return

if __name__ == "__main__":
    main()