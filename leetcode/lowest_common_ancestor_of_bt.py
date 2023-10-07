"""
LC: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
YT: https://www.youtube.com/watch?v=13m9ZCB8gjw

Approach:
(not easy to explain, watch the YT video)
- recursive, bottom up approach
- search for the two nodes
- the first node we find who's left and right children have found the nodes, it's an ancestor
- it's also the lowest common ancestor since we are doing a bottom-up approach,
  so the first occurence where node.left is not None and node.right is not None means node is LCA

- the trick here is that if only one of the child returned a node, re-return that node
- eventually that node will be bubled up to the LCA

- in short:
  * if both left and right children found nodes, return current node
  * if both children returned None, return None
  * otherwise, if one child returned a node, return that node

Time complexity: O(n)
- where n = number of nodes in the tree
- we are visiting n nodes in the worst case, and doing O(1) work per node

Space complexity: O(h)
- where h = height of the binary tree
- to use the stack space
- in the worst case, O(h) will be O(n) if the tree is left or right skewed
"""


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # base case
    if not root:
        return None
    
    # found one of the nodes we are searching for, so return it
    if root == p or root == q:
        return root
    
    # look for p and q in the left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # if p and q are found in left and right subtrees, current node is an ancestor
    # it's also the lowest common ancestor because we are going bottom up
    if left and right:
        return root
    
    # leaf node or none of the children found p or q, so return None
    if not left and not right:
        return None
    
    # if either of the children have found at least one of p or q, return whatever is found
    return left if left else right
