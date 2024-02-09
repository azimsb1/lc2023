'''
LC: https://leetcode.com/problems/contains-duplicate/

Approach:
- maintain a "seen" hash set
- for each number:
    * if we have already seen it, return True
    * otherwise, add it to the set in case we see it again in the future
- at the end, return false. This means no num has been seen more than once

Time complexity: O(n)
- where n = len of nums
- we are looking at each number at most once

Space complexity: O(n)
- where n = len of nums
- in the worst case when all numbers are unique, we will store them all once in the seen hash set
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
