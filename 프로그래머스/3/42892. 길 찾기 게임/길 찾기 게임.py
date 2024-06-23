import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, num, x):
        self.nodeNum = num
        self.x = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.pre = []
        self.post = []
    def insert(self, num, x):
        new_node = Node(num,x)
        if self.root == None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if current_node.x < x: #right
                if current_node.right == None:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right
            else: #left
                if current_node.left == None:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left

    def preorder(self, node):
        if node == None:
            return
        self.pre.append(node.nodeNum)
        self.preorder(node.left)
        self.preorder(node.right)
            
    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        self.post.append(node.nodeNum)
    
def solution(nodeinfo):
    sorted_y_info = sorted(nodeinfo, key=lambda x:x[1], reverse=True)
    binaryTree = BinaryTree()
    for i in sorted_y_info:
        binaryTree.insert(nodeinfo.index(i)+1,i[0])

    binaryTree.preorder(binaryTree.root)
    binaryTree.postorder(binaryTree.root)
    answer = [binaryTree.pre, binaryTree.post]
    return answer