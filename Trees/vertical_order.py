from collections import deque, defaultdict

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

    def vertical_order_traversal(self):
        if not self.root:
            return []

        nodes = defaultdict(lambda: defaultdict(list))
        todo = deque([(self.root, 0, 0)])  # node, column, row

        while todo:
            node, x, y = todo.popleft()
            nodes[x][y].append(node.val)

            if node.left:
                todo.append((node.left, x - 1, y + 1))
            if node.right:
                todo.append((node.right, x + 1, y + 1))

        ans = []
        for x in sorted(nodes):  # columns from left to right
            col = []
            for y in sorted(nodes[x]):  # rows from top to bottom
                for val in sorted(nodes[x][y]):
                    col.append(val)
            ans.append(col)
        return ans
    
    def top_view(self):
        if not self.root:
            return []
        mpp = {}  # key: line (column), value: node.val
        q = deque([(self.root, 0)])  # (node, column)

        while q:
            node, line = q.popleft()
            if line not in mpp:
                mpp[line] = node.val  # Pehli baar hi wo node dikhai dega

            if node.left:
                q.append((node.left, line - 1))
            if node.right:
                q.append((node.right, line + 1))

    # Columns ko left se right sort karke result nikaalo
        result = [mpp[x] for x in sorted(mpp)]
        return result

# Usage:
values = input().split()  # For example: 10 20 30 None 40 None 50
tree = Tree()
tree.build_from_level_order(values)
result = tree.vertical_order_traversal()
print(result)
print(tree.top_view())


