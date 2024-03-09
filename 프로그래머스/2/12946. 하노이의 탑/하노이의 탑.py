def hanoi(N,a,b,c,ans):
    if N == 1:
        ans.append([a,c])
    else:
        hanoi(N-1,a,c,b,ans)
        ans.append([a,c])
        hanoi(N-1,b,a,c,ans)

def solution(n):
    answer = []
    hanoi(n,1,2,3,answer)
    return answer