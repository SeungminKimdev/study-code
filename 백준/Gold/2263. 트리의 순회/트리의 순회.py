import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

def preOrderDetect(startIn, endIn, startPost, endPost):
    if startIn > endIn or startPost > endPost:
        return
    
    root = postOrder[endPost]
    preOrder.append(root)
    rootIndex = inOrderIndex[root]
    leftSize = rootIndex - startIn
    
    preOrderDetect(startIn, rootIndex - 1, startPost, startPost + leftSize-1)
    preOrderDetect(rootIndex + 1, endIn, startPost + leftSize, endPost-1)

def main():
    n = int(input())
    global inOrder, postOrder, inOrderIndex, preOrder
    
    inOrder = input().split()
    inOrderIndex = {value: index for index, value in enumerate(inOrder)}
    postOrder = input().split()
    preOrder = []
    
    preOrderDetect(0, n - 1, 0, n - 1)
    print(" ".join(map(str, preOrder)))
    return

if __name__ == "__main__":
    main()