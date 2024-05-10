"""
LC: https://leetcode.com/problems/merge-two-sorted-lists

Approach:
- simple pointer manipulation
- building a new list by picking the smaller node from the two lists each time
- some tricks:
    * using a dummy_node to avoid initializing head, and easier return at the end
    * checking if either lists have any nodes left, and just append that list

Algorithm at a glance:
- start with a dummy node to simplify handling the head of the new list
- iterate over lists:
    a. choose the smaller node from the heads of list1 and list2
    b. append to the (newly being created) merged list
- finally append any remaining nodes from either list

Time complexity: O(n + m)
- where n = length of list1 and m = length of list2
- every node in each list is visited once while the new list is being created
- so linear time complexity

Space complexity: O(1)
- just pointer adjustments
- no new nodes are created, only the existing ones are relinked
- also, no allocation of additional space that grows with the input size
- so, constant space complexity
"""


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # dummy node's next will be the start of the sorted list
    dummy = ListNode(-1)
    # current will point to the tail of the newly being built sorted list
    current = dummy

    # loop until both list have some node(s)
    while list1 and list2:
        # pick the smaller one, add after current, and increment
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        # progress current one step forward
        current = current.next
    
    # if any of the two list have any remaining nodes, add them to the end of current
    # note: not possible that both have some nodes, otherwise while loop would not have exited
    current.next = list1 if list1 else list2

    # dummy node's next is the start of the new list
    return dummy.next
