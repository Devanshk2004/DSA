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

    def max_height(self, node):
        if node is None:
            return 0
        lh = self.max_height(node.left)
        rh = self.max_height(node.right)
        return 1 + max(lh, rh)

    def diameter(self, node):
        if node is None:
            return 0

        lh = self.max_height(node.left)
        rh = self.max_height(node.right)

        left_diameter = self.diameter(node.left)
        right_diameter = self.diameter(node.right)

        return max(lh + rh, max(left_diameter, right_diameter))

    # --- O(n) Diameter Function ---
    def diameter_optimized(self):
        def height_and_diameter(node, maxi):
            if node is None:
                return 0
            lh = height_and_diameter(node.left, maxi)
            rh = height_and_diameter(node.right, maxi)
            maxi[0] = max(maxi[0], lh + rh)
            return 1 + max(lh, rh)
        maxi = [0]
        height_and_diameter(self.root, maxi)
        return maxi[0]
    

# --- Main ---
# Read input
values = input().split()

tree = Tree()
tree.build_from_level_order(values)

# Compute and print maximum height
height = tree.max_height(tree.root)
print("Maximum height of the tree:", height)

# Compute and print diameter (O(n^2) version)
diameter = tree.diameter(tree.root)
print("Diameter of the tree (O(n^2)):", diameter)

# Compute and print diameter (O(n) version)
diameter_opt = tree.diameter_optimized()
print("Diameter of the tree (O(n)):", diameter_opt)
