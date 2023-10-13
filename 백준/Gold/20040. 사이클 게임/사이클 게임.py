import sys
input = sys.stdin.readline

class Unionfind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.ans = 0
        self.end = False

    def findP(self,p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self,p,q):
        rootP = self.findP(p)
        rootQ = self.findP(q)
        if rootP == rootQ:
            self.end = True
        else:
            if rootQ < rootP:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
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