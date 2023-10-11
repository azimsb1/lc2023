"""
LC: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
YT: https://www.youtube.com/watch?v=TIoCCStdiFo
YT: https://www.youtube.com/watch?v=gs2LMfuOR9k

Note: this can also be solved by the algorithm to find the LCS of a Binary Tree, but it doesn't take into the account the special propery of binary Search tree: left < root < right

Approach:
- assumption: all nodes are unique

- trick: to find the LCA, we find the node where there is a split, where p and q are going in separate subtrees
- in other words, we are looking for the node from which p and q diverge in different paths

- for every node:
  * if p or q is found, that's the ancestor
  * if both p and q are smaller than root, look in the left subtree
  * else if both p and q are bigger than root, look in the right subtree
  * otherwise, we know that root lies between p and q
  * and this is where the path diverges (because p will be in left/right and q will be in the other half)
  * so, this node is the lowest common ancestor

Time complexity: O(h)
- where h = height of the binary Search tree
- in each function call, we either find the node, or we eliminate half of the tree
- we will visit one node for each level in the tree, so the time complexity is height of the tree

Space complexity: O(h):
- where h = height of the binrary Search tree
- this is due to the use of the call stack for recursive calls
"""


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # base case
    if not root:
        return None
    
    # found the node, so it's the LCA
    if root.val == p.val or root.val == q.val:
        return root
    
    # both p and q are smaller than root, so they must be in the left subtree
    if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
    
    # both p and q are bigger than root, so they must be in the right subtree
    elif p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    
    # reached here means that root lies between p and q
    # so root is the LCA
    else:
        return root
