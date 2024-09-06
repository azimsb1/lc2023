"""
LC: https://leetcode.com/problems/longest-consecutive-sequence/

Approach:
- the key requirement is to do this in O(n) time, so we cannot sort it

- the key idea is that each number is either:
    a. the start of a new streak
    b. part of an existing streak
- the data structure of choice is a set (of numbers), since we can look up numbers in O(1) time

- so, for each number, we check if it's the start of a new streak, i.e. (num-1) NOT in set
- if it is, we continue making a streak until we can, by finding (num+1) in the set
- when a streak ends, we update the longest streak seen so far, if the current streak is longer

- key insight:
    * we do not attempt to start a new streak (and continue until it ends) for each number
    * this would be O(n^2) time
    * we only start counting a streak when the current number is the beginning of a sequence (i.e., num-1 is not in the set)
    * this which ensures that we only consider each sequence once.
    
Time complexity: O(n)
* where n = length of input `nums`
* since we look at each streak only once, we look at each number at most twice
* so, the time complexity if O(n)

Space complexity: O(n)
* where n = length of input `nums`
* since we will make a set of nums for O(1) look ups

"""


# O(n) solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums:
            # new streak
            if (num - 1) not in nums_set:
                current = 0
                # continue while there is a streak
                while num in nums_set:
                    current += 1
                    num += 1
                # check if the current streak is bigger than the longest streak
                longest = max(longest, current)

        return longest


# O(n log n) solution
# class Solution:
# def longestConsecutive(self, nums: List[int]) -> int:
#     # edge case
#     if not nums:
#         return 0

#     # sort to track streaks
#     nums.sort()
#     current, longest = 1, 0

#     for i in range(1, len(nums)):
#         # if the number is same as before, continue current streak but don't increment its count
#         if nums[i] == nums[i-1]:
#             continue
#         # if the number is exactly one more than before, add 1 to the current streak
#         elif nums[i] == nums[i-1] + 1:
#             current += 1
#         # current streak broke - check for the longest streak and reset current streak
#         else:
#             longest = max(longest, current)
#             current = 1

#     # if a streak didn't break while iterating, longest wouldn't have been set
#     longest = max(longest, current)

#     return longest
