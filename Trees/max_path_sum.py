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

    # --- Maximum Path Sum Function ---
    def max_path_sum(self):
        self.max_sum = float('-inf')

        def dfs(node):
            if node is None:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)

        dfs(self.root)
        return self.max_sum

# --- Main ---
# Read input
values = input().split()

tree = Tree()
tree.build_from_level_order(values) 

# Example: Print maximum path sum
print("Maximum path sum in the tree:", tree.max_path_sum())
