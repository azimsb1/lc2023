"""
LC:
YT: https://www.youtube.com/watch?v=OnSn2XEQ4MY

Approach: https://leetcode.com/problems/invert-binary-tree/
- solving this recursively using DFS
- for each node, swap its left and right children
- and then run this algorithm recursively on the left subtree and right subtree so that _their_ children are also swapped
- this will invert the binary tree

Runtime: O(n)
- where n = number of nodes
- for each n nodes, we are doing O(1) amount of work

Space complexity: O(h)
- where h = height of the binary tree
"""


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # base case
    if not root:
        return None

    # swap left and right subtrees
    root.left, root.right = root.right, root.left
    
    # recursively invert the left subtree
    self.invertTree(root.left)
    # recursively invert the right subtree
    self.invertTree(root.right)
    
    # return the inverted tree rooted at "root"
    return root
