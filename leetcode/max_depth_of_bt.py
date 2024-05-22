"""
LC: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Approach 1:
-----------
- recurive DFS
- max depth of a tree rooted at node is 1 + max of depth of left and depth of right subtrees
- 1 because current node adds 1 to the depth
  and then max of the depth of the subtree rooted at node.left and depth of the subtree rooted at node.right
- base case is when a None node is reached, whose depth is 0

Time complexity: O(n) where n = # of nodes

Space complexity: O(h) where h = height of the bt
- in a balanced binary tree, h = log n, so space complexity would be O(log n)
- in a skewed binray tree, h = n, so the space complexity would be O(n)
- generally, space complexity of dfs on a binary tree can be described as O(h)

Approach 2:
-----------
- BFS, level order traversal
- the idea is that the total number of levels of a binaruy tree is the same as its max depth

- usual BFS using a queue and traversing each level
- everytime a level is traversed, # of levels is incremented
- at the end, the # of levels is returned as the max depth

Time complexity: O(n)
- where n = number of nodes
- each node is visited exactly once

Space complexity: O(N)
- where n = number of nodes
- at any given time, the maximum number of nodes stored in the queue is N/2
- this happens at the widest level, which is the last level
- which is why the space complexity scales linearly, giving O(N/2) = O(N)

- general rule: the space complexity for BFS is determined by the maximum breadth of the tree
"""


# Approach 1 - Recursive DFS
def maxDepth(self, root: Optional[TreeNode]) -> int:
  # base case - None node is reached, depth is 0
  if not root:
      return 0
  
  # max depth of left subtree
  depth_left = self.maxDepth(root.left)
  # max depth of right subtree
  depth_right = self.maxDepth(root.right)

  # depth is 1 (cur node) + max of the left or right children's depth
  return 1 + max(depth_left, depth_right)


'''
# Approach 2: Iterative BFS, level order traversal
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    levels = 0
    queue = deque([root])

    while queue:
        # traverse current level
        for _ in range(len(queue)):
            node = queue.popleft()
            # add left and right children if exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # increment number of levels seen so far
        levels += 1

    # total number of levels == max depth
    return levels
'''
