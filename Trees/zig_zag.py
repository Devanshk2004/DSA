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

    def zig_zag(self ,node):
        if not node:
            return []
        
        result = []
        nodes_queue = deque([node])
        left_to_right = True

        while nodes_queue:
            size = len(nodes_queue)
            row = [0] * size

            for i in range(size):
                current = nodes_queue.popleft()
                index = i if left_to_right else (size - 1 - i)
                row[index] = current.val

                if current.left:
                    nodes_queue.append(current.left)
                if current.right:
                    nodes_queue.append(current.right)
            
            result.append(row)
            left_to_right = not left_to_right

        return result


values = input().split()  # for example: 10 20 30 None 40 None 50

tree = Tree()
tree.build_from_level_order(values)

zigzag_result = tree.zig_zag(tree.root)
for level in zigzag_result:
    print(*level)


# test here maybe