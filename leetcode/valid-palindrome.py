"""
LC: https://leetcode.com/problems/valid-palindrome/

Approach:
- two pointer approach with left and right
- check chars until left and right meet

- if they meet without any problems, it's a palindrome, so return true
- if chars are not same, it's not a valid palindrome, so return false

- for each character, make it lowercase and skip it if it's not an alphanumeric char

Time complexity: O(n)
- where n = length of string
- each character is looked at most once
- so linear space complexity

Space complexity: O(1)
- algorithm runs in place and no aux space is required
- just the two variables for two pointers
- so constant space complexity

Note:
- initially implemented an `is_alphanumeric` function
- but later found out that there is a built in `isalnum()` function
- so used the built in function but kept the custom implementation for knowledge purposes
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left and right pointers
        left, right = 0, len(s) - 1

        # while the two pointers meet
        while left < right:
            # skip all non alphanumeric chars at left
            while left < right and not s[left].isalnum():
                left += 1

            # skip all non alphanumeric chars at right
            while left < right and not s[right].isalnum():
                right -= 1

            # if not same, return false
            if s[left].lower() != s[right].lower():
                return False

            # increment left, decrement right
            left += 1; right -= 1

        # outside of while loop means both pointers met without problems, so return true
        return True
    
    """
    def alphanumeric(self, char):
        char = char.lower()
        # between "0" and "9"
        if char in set(["0","1","2","3","4","5","6","7","8","9"]):
            return True
        # between "a" and "z"
        return (ord(char) - ord('a') >= 0) and (ord(char) - ord('z') <= 0)
    """
