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
    
    def check_balance(self, node):
        if node is None:
            return 0
        
        lh = self.check_balance(node.left)
        if lh == -1:
            return -1
        
        rh = self.check_balance(node.right)
        if rh == -1:
            return -1
        
        if abs(lh - rh) > 1:
            return -1
        
        return max(lh, rh) + 1
    
    def is_balanced(self, root):
        return self.check_balance(root) != -1
    
values = input().split()

tree = Tree()
tree.build_from_level_order(values)

# Compute and print maximum height
is_balanced = tree.is_balanced(tree.root)
print("The tree is balanced",is_balanced)   



            


     