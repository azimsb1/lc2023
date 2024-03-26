"""
LC: https://leetcode.com/problems/subtree-of-another-tree/

Approach:
- this problem utilizes the algorithm developed in leetcode 100 (Same Tree):
  https://leetcode.com/problems/same-tree/description/

- the idea is to check for a node `n` in the first tree
- such that a subtree rooted at `n` is the _same tree_ as the subtree from parameter

- so, we do a depth first search to recursively check each node `n`
- for each node `n` in the first tree, we check if the subtree rooted at `n` is identical to `subRoot` using the "same tree" logic

- to summarize:
    * dfs to explore each potential matching starting point
    * recursive comparison to check structural and value equivalence between two trees (aka "same tree")


Time complexity: O(n * m)
- where n = # of nodes in the first tree
- and m = # of nodes in the second tree
- this is bacause in the worst case, for each node in the first tree, we will check all nodes in the second tree

Space complexity: O(h)
- where h = height of the first tree
- to use the call stack for recursion
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if root is None, subRoot must be None
        if not root:
            return not subRoot
        
        # reaches here when root is NOT None, so subRoot cannot be None
        if not subRoot:
            return False
        
        # are first tree rooted at "root" and subTree same?
        same = self.sameTree(root, subRoot)
        # if same, that means subTree is a subtree of first ree
        if same:
            return True
        # if not, check if subTree is a subtree of the left subtree of root
        # of subTree is a subtree of the right subree of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # same as leetcode 100. Same Tree
    def sameTree(self, p, q):
        # if both trees are None, they are same
        if not p and not q:
            return True
        # if both are NOT None but one of them is None, they CANNOT be same
        if not p or not q:
            return False
        # same when both nodes have the same value and identical left and right children with each other
        return p.val == q.val and self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
