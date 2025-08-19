from treenode import TreeNode
from collections import deque


def print_all_nodes_bfs(root: TreeNode):
    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        # do some logic here on current level
        # ...

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            # do some logic here on the current node
            print(node.val, end=" ")

            # put the next level node in the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        print()


def print_all_nodes_dfs(root: TreeNode):
    stack = [root]
    while stack:
        node = stack.pop()

        # do some logic here on the current node
        print(node.val, end=" ")

        # put the next level node in the stack
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    print()


root = TreeNode.create_from_list([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])
print_all_nodes_bfs(root)
# print_all_nodes_dfs(root)
