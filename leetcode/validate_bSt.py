"""
LC: https://leetcode.com/problems/validate-binary-search-tree/
YT: https://www.youtube.com/watch?v=s6ATEkipzow&t=595s

Approach:
- just checking left.val < root.val < right.val is not sufficient
- ALL the nodes the left subtree have to be smaller then the root and ALL of the nodes in the right subtree have to be bigger than the root

- so, we solve this recursively with the help of min and max values
- in every function call, the following conditions must satisfy:
  * root must be in between the min and max values
  
  * all of the nodes in the left subtee must be smaller than the root, so the max_val is updated to the root
    (note that the previous left boundary / min_val still holds true - this is important)

  * all of the nodes in the right subtree must be bigger than the root, so the min_val is updated to the root
    (note that the previous right boundary / max_val still holds true.
    Think cur node is the left child of the original root. All of the _right_ children of the cur node must still be smaller than the original root.
    So, the right boundary / max_val stays the same)

Time complexity: O(n)
- where n = number of nodes in the bSt
- looking at all the nodes

Space complexity: O(h)
- where h = height of the bSt
"""


def isValidBST(root: Optional[TreeNode]) -> bool:
    # for the root of the original tree, there is no limit to what the node's val could be
    # so the min_val is -inf and the max_val is +inf
    return isValidBSTHelper(root, -inf, inf)

# Helper recursive function
def isValidBSTHelper(root, min_val, max_val):
    # base case
    if not root: return True

    # node's value lies between min and max
    if not (min_val < root.val < max_val): return False
    
    """
    not required
    # if (root.left and root.val < root.left.val) or \
    #     (root.right and root.val > root.right.val): return False
    """
    
    # a. when looking at left subtree, the max_val changes to the root's val (and min_val is carried forward)
    # b. and when looking at the right subtree, the min_val changes to the root's val (and max_val is carried forward)
    return isValidBSTHelper(root.left, min_val, root.val) and \
        isValidBSTHelper(root.right, root.val, max_val)
