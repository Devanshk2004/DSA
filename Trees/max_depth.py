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
    #Normal
    def max_height(self, node):
        if node is None:
            return 0
        left_height = self.max_height(node.left)
        right_height = self.max_height(node.right)
        return 1 + max(left_height, right_height)
    

    #Level order
    def max_height_level_order(root):
       if not root:
        return 0
       q = deque([root])
       height = 0
       while q:
        level_size = len(q)
        for _ in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        height += 1
        return height

# --- Main ---
# Read input
values = input().split()

tree = Tree()
tree.build_from_level_order(values)

# Compute and print maximum height
height = tree.max_height(tree.root)
print("Maximum height of the tree:", height)
