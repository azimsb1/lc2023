"""
LC: https://leetcode.com/problems/reverse-linked-list/

NOTE: This can also be solved recusrively. Refer to the solution here:
- https://leetcode.com/problems/reverse-linked-list/submissions/1202075065/
- (needs to be loged in as azimsb120)

Approach (Iterative):
- using 3 pointers to help us: previous, current, and next
- simply adjust the pointers so that each node's next becomes its previous one
- don't forget to save the next node first so the pointer to it is not lost

- for each node, follow these 4 steps:
    a. save the pointer to its next node
    b. point its next to its previous node
    c. progress previous 1 step so precvious points to it
    d. progress it 1 step so the next node becomes current and can be worked with

Time Complexity: O(n)
- where n = # of nodes
- each node is visited once, and is pointers are tweaked
- so linear time complexity

Space complexity: O(1)
- just using helper variables/pointers
- and no aux space is used
- so constant space complexity
"""


# Iterative
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # previous node of of the current node in each iterations
    # at the end, the new head will be this
    prev = None
    # points to each node one by one with each iteration
    cur = head

    # while nodes left to look at
    while cur:
        # save the next node so that pointer is not lost
        next = cur.next
        # current's node new next will be its previous node
        cur.next = prev
        # now set the previous node to the current node for the current node's next
        prev = cur
        # now look at the next node in the list
        cur = next
    
    # at the end, cur will point to None, and prev will point to the last node of the original list (now new head)
    return prev
