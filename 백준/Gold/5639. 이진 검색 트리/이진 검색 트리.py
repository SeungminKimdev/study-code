import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def changeSearch(tree, start, end):
    if start >= end:
        return
    
    check = tree[start]
    endP = end
    for i in range(start+1,end):
        if tree[i] > check:
            endP = i
            break
        
    changeSearch(tree, start+1, endP)
    changeSearch(tree, endP, end)
    print(check)
    return

def main():
    tree = []
    for line in sys.stdin:
        tree.append(int(line))
    length = len(tree)
    changeSearch(tree,0,length)
    return

if __name__ == "__main__":
    main()