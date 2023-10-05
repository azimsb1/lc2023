"""
Serialization:
  - we are going to use a pre-order traversal
  - in each call, process a single node, and then defer all of the other work for recursion
  - for a given node, its serialization is going to look like: node.val + serialized_left + serialized_right

  - we use a comma as a delimeter to separate these numbers

Deserialization:
  - use a helper method with a queue that keeps track of the next node to progress
  - in each iteration, make a node out of the value
  - then set left by deserializing left and set right by deserializing right
  - this is also preorder: process noode, then process all of left, and then process all of right

  - the queue in every call keeps the freshest progress of the next node to progress
  - every single stack frame knows where to pick up where the other frame left off

  - since 'X' denotes a Null node, it knows exactly where the subtree ends

Time and space complexity: O(n)
- where n = number of nodes
"""

def serialize(root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    # base case, Null node
    if not root:
        return 'X,'
    
    # preorder traversal: self + serialized left + serialized right
    serialized_left = serialize(root.left)
    serialized_right = serialize(root.right)

    return str(root.val) + ',' + serialized_left + serialized_right


def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    # queue will maintain the next node to process
    queue = deque(data.split(','))
    # call the helper recursive method
    return deserialize_helper(queue)


def deserialize_helper(queue):
    # pop the next fresh item to process
    item = queue.popleft()

    # base case, Null node
    if item == 'X':
        return None
    
    # else, process the node
    node = TreeNode(int(item))

    # serialize left and right children
    node.left = deserialize_helper(queue)
    node.right = deserialize_helper(queue)

    # return node with its children already set
    return node
