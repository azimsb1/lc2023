"""
LC: https://leetcode.com/problems/binary-search

Approach:
- binary search, one of the most important topics for coding interviews

- special propery: numbers are sorted. we will take advantage of this
- in every search iteration, we cut the searh interval in half
- this is because in a sorted list, for a given element e:
    * everything to the left of e will be smaller or equal to e
    * everything to the right of e will be greater or equal to e
- so, if the element you're looking for is less than the item in the middle:
    * you continue to search the left half;
- otherwise, you search the right half

- note: duplicates do not exist in this question
- if duplicates were allowed:
    * algorithm would be the same if we do NOT care about the index of the element
    * algorithm NEEDS TO BE adapted if we need to find the a specific occurrence (first, last, etc.) of that element

Time complexity: O(log N)
"""

def search(self, nums: List[int], target: int) -> int:
    # left and right boundary for search space
    left, right = 0, len(nums) - 1

    while left <= right:
        # find mid
        mid = left + ((right-left)//2)
        # target found
        if nums[mid] == target:
            return mid
        # target is in the left half, move right boundary
        if target < nums[mid]:
            right = mid - 1
        # target is in the right half, move left boundary
        else:
            left = mid + 1

    # no solution
    return -1
