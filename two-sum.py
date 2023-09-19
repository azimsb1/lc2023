"""
LC: https://leetcode.com/problems/two-sum

Approach:

We want to find a solution in 1 pass. To accomplish this, we maintain a "seen" hashmap of numbers and their indices.
For each number, find its complement. Complement = what needs to be added to the number so that sum is target?
If complement is seen before, take complement's index from the map and return with index i.
Otherwise, add the number and its index to the seen map, as this will be some other number's complement in the future.

Time Complexity: O(n)
- where n = length of nums
- doing just one pass

Space complexity: O(n)
- where n = length of nums
- in the worst case, we will store n - 1 numebrs in the hash map
"""

class Solution(object):
    def twoSum(self, nums, target):
        # map will remember the numbers seen before and their indices
        seen = {}

        for i in range(len(nums)):
            # complement is difference between target and nums[i]
            complement = target - nums[i]
            # if seen complement before, return its index and i
            if complement in seen:
                return [seen[complement], i]
            # otherwise, add nums[i] and i to the seen map
            seen[nums[i]] = i

        # no solution
        return [-1, -1]                
