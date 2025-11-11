#same traversal using stack

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

def preorder_stack(root):
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inorder_stack(root):
    result = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def postorder_stack(root):
    if not root:
        return []
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    return [node.val for node in reversed(stack2)]

def level_order_queue(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result

# ---------------- MAIN ----------------

# Input example: 8 3 10 1 6 None 14 None None 4 7 13 None
values = input("Enter level-order with None for missing: ").split()

tree = Tree()
tree.build_from_level_order(values)

# Run all traversals
pre = preorder_stack(tree.root)
ino = inorder_stack(tree.root)
post = postorder_stack(tree.root)
lev = level_order_queue(tree.root)

# Print results
print('Preorder:   ', ' '.join(map(str, pre)))
print('Inorder:    ', ' '.join(map(str, ino)))
print('Postorder:  ', ' '.join(map(str, post)))
print('LevelOrder: ', ' '.join(map(str, lev)))
