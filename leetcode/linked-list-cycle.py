"""
LC: https://leetcode.com/problems/linked-list-cycle

Approach:
- tortoise and hare algorithm
- there is a slow pointer (tortoise), which moves ONE step at a time
- there is a fast pointer (hare), which moves TWO steps at a time
- if there a cycle, the fast pointer will eventually meet the slow pointer
- if there is NOT a cycle, the fast pointer will fall off the list

Time complexity: O(n)
- where n = number of nodes in the list
- if it's NOT cyclic, fast will reach the end of the list in n/2 steps
- note: a bit nuanced, read online how the time complexity is O(n+k), where k = length of cycle 
"""

def hasCycle(head: Optional[ListNode]) -> bool:
    # edge case - empty list - NOT cyclic
    if not head:
        return False
    
    # slow and fast pointers, move one and two steps at a time, respectively
    slow, fast = head, head.next

    # while fast has not reached the end of the list
    # (and has a valid next node)
    while fast and fast.next:
        # pointers met, that means there IS a cycle
        if slow == fast:
            return True
        
        # slow pointer moves one step forward
        slow = slow.next
        # fast pointer moves two steps forward
        fast = fast.next.next
    
    # reached end of list without meeting, which means NOT cyclic
    return False
