from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)

    def preorder(self, node, result):
        if node is None: return
        result.append(node.val)
        self.preorder(node.left, result)
        self.preorder(node.right, result)

    def inorder(self, node, result):
        if node is None: return
        self.inorder(node.left, result)
        result.append(node.val)
        self.inorder(node.right, result)

    def postorder(self, node, result):
        if node is None: return
        self.postorder(node.left, result)
        self.postorder(node.right, result)
        result.append(node.val)

    def level_order(self):
        if not self.root: return []
        result = []
        q = deque([self.root])
        while q:
            node = q.popleft()
            result.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return result

# Read input
nums = list(map(int, input().split()))

tree = Tree()
for val in nums:
    tree.insert(val)

# Traversals
pre = []
tree.preorder(tree.root, pre)
ino = []
tree.inorder(tree.root, ino)
post = []
tree.postorder(tree.root, post)
lev = tree.level_order()

# Output
print('Preorder:   ', ' '.join(map(str, pre)))
print('Inorder:    ', ' '.join(map(str, ino)))
print('Postorder:  ', ' '.join(map(str, post)))
print('LevelOrder: ', ' '.join(map(str, lev)))
