import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

class Unionfind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.ans = 0
        self.end = False

    def findP(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.findP(self.parent[p])
        return self.parent[p]

    def union(self,p,q):
        rootP = self.findP(p)
        rootQ = self.findP(q)
        if rootP == rootQ:
            self.end = True
        else:
            if self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            elif self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            else:
                self.parent[rootP] = rootQ
                self.rank[rootQ] += 1
        self.ans += 1

if __name__ == '__main__':
    n, m = map(int,input().split())
    unionfind = Unionfind(n)
    for _ in range(m):
        a, b = map(int,input().split())
        if unionfind.end:
            break
        unionfind.union(a,b)

    if not unionfind.end:
        print('0')
    else:
        print(unionfind.ans)