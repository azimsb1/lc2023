"""
LC: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Approach:
- recurive DFS
- max depth of a tree rooted at node is 1 + max of depth of left and depth of right subtrees
- 1 because current node adds 1 to the depth
  and then max of the depth of the subtree rooted at node.left and depth of the subtree rooted at node.right
- base case is when a None node is reached, whose depth is 0

Time complexity: O(n) where n = # of nodes
Space complexity: O(h) where h = height of the bt
"""

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
