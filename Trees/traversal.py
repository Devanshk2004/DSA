from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def build_from_level_order(self, values):
        if not values or values[0] == 'None':
            self.root = None
            return

        iter_vals = iter(values)
        self.root = TreeNode(int(next(iter_vals)))
        q = deque([self.root])

        while q:
            node = q.popleft()
            try:
                left_val = next(iter_vals)
                if left_val != 'None':
                    node.left = TreeNode(int(left_val))
                    q.append(node.left)

                right_val = next(iter_vals)
                if right_val != 'None':
                    node.right = TreeNode(int(right_val))
                    q.append(node.right)
            except StopIteration:
                break

    def preorder(self, node, result):
        if node is None: return
        result.append(node.val)
        self.preorder(node.left, result)
        self.preorder(node.right, result)

    #To check if trees are identical
    
    #def are_trees_identical(tree1, tree2):
    #    result1 = []
    #    result2 = []
    #    tree1.preorder(tree1.root, result1)
    #   tree2.preorder(tree2.root, result2)
    #    return result1 == result2


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

# --- Main ---
# Read input
values = input().split()  # for example: 10 20 30 None 40 None 50

tree = Tree()
tree.build_from_level_order(values)

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
