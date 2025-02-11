import sys
input = sys.stdin.readline

def main():
    n = int(input())
    m = int(input())
    friends = [[] for _ in range(n+1)]
    not_friends = [[] for _ in range(n+1)]
    for _ in range(m):
        relation, p, q = input().split()
        p, q = int(p), int(q)
        if relation == 'F': # friend
            friends[p].append(q)
            friends[q].append(p)
        else: # not friend
            not_friends[p].append(q)
            not_friends[q].append(p)
    
    for student in not_friends:
        length = len(student)
        for j in range(length-1):
            for k in range(j+1, length):
                friends[student[j]].append(student[k])
                friends[student[k]].append(student[j])
    
    answer = 0
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            answer += 1
            visited[i] = True
            q = [i]
            while q:
                now = q.pop()
                for friend in friends[now]:
                    if not visited[friend]:
                        visited[friend] = True
                        q.append(friend)
    
    print(answer)

if __name__ == "__main__":
    main()