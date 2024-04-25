"""
LC: https://leetcode.com/problems/valid-parentheses

Approach:
- simple, iterative solution, by looking at each char one by one

- data structure: stack
    * everytime there is an open bracket, this needs to be "remembered" for when there is a closed bracket
    * recency is also important, because close needs the _same_ type of open most recently
    * so stack is used, LIFO

- for each bracket
    * if it's open, just add it to the stack and wait for it's close bracket
    * if it's close, make sure the same type of open exists, and at the top of stack (most recent)

- at the end, ensure that the stack is empty
- because non-empty stack means there exists open brackets that have not been closed

- useful trick (but optional) for early exit: odd length means it's invalid
- (because every open needs a closed and vice versa)

Time complexity: O(n)
- where n = length of string
- we look at each bracket just once

Space complexity: O(1)
- the onlyu extra space we use is for the pairs hashmap
- and it's size is constant, no matter how big the input gets
- so, constant space (O(1))
"""

def isValid(s: str) -> bool:
    # early exit - odd length means it's not valid
    if len(s)%2 != 0:
        return False

    # tracks open brackets
    stack = []

    # open-close pairs
    pairs = {')': '(', ']': '[', '}': '{'}

    # look at each bracket
    for bracket in s:
        # if closed
        if bracket in pairs:
            # assert that most recent and same type of open exists
            if not stack or stack.pop() != pairs[bracket]:
                return False
        # if open
        else:
            stack.append(bracket)
    
    # assert that all open brackets have been closed
    return not stack
