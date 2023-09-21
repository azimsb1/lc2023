"""
LC: https://leetcode.com/problems/binary-tree-level-order-traversal/

Approach:
- BFS, using a queue
- for each iteration of the while loop, process all the nodes for that level (using len(queue))
- process a node = save its value, and enqueue its children
"""

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    # this will store all levels
    levels = []

    # edge case - root is None
    if not root:
        return levels

    # FIFO queue for BFS
    q = deque([root])

    # keep traversing until the queue is empty
    while q:
        # this will store all the nodes at one level
        level = []
        # len helps us know how many nodes are there at the current level
        for _ in range(len(q)):
            # dequeue the node
            node = q.popleft()
            # if not None, add it's value to the current level, and enqueue its children
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)

        # if current level is non-empty, add it to the list of levels
        if level:
            levels.append(level)

    return levels
