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

        from collections import deque
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

    def is_leaf(self, node):
        return node and not node.left and not node.right

    def add_left_boundary(self, node, res):
        curr = node.left
        while curr:
            if not self.is_leaf(curr):
                res.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def add_leaves(self, node, res):
        if node is None:
            return
        if self.is_leaf(node):
            res.append(node.val)
            return
        self.add_leaves(node.left, res)
        self.add_leaves(node.right, res)


    def add_right_boundary(self, node, res):
        curr = node.right
        temp = []
        while curr:
            if not self.is_leaf(curr):
                temp.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(temp[::-1])  # Reverse to get bottom-up

    def boundary_traversal(self):
        res = []
        if not self.root:
            return res
        if not self.is_leaf(self.root):
            res.append(self.root.val)
        self.add_left_boundary(self.root, res)
        self.add_leaves(self.root, res)
        self.add_right_boundary(self.root, res)
        return res

# Usage:
values = input().split()  # Example: 1 2 3 4 5 None 6 None None 7 8
tree = Tree()
tree.build_from_level_order(values)
boundary = tree.boundary_traversal()
print(*boundary)
