"""
LC: https://leetcode.com/problems/product-of-array-except-self/description/

Approach:
- the key requirement is to not use the division operator

- they key observation is that the product of array except the element at index i = product of arr[:i] times product[i+1:]
- that is, is the product of:
    (a) product of all elements to the left of i (excluding i)
    (b) product of all elements to the right of i (excluding i)

- another observation is that the product of arr[:i] = product of arr[:i-1] * nums[i]

- so, we will create 2 arrays:
    (a) a left array: where left[i] = product of all elements to the left of i
    (b) a right array: where right[i] = product of all elements to the right of i
- then, the product[i] is just the product of left[i] and right[i]

Time complexity: O(n)
- where n = length of the input array
- O(n) to generate left + O(n) to generate right + O(n) to generate product
- so, time complexity is O(3n) = O(n)

Space complexity: O(n)
- where n = length of the input array
- excluding the result array, we are using O(2n) = O(n) aux space
- so, space complexity is O(n)

Note:
- on Leetocode, there is a O(1) space solution available
- excluding the space required for the result array
- simply explained approach:
    * calculate the left-side product on the fly
    * then calculating the right-side product in a second pass, updating the result array in place
    * this way, the need for the left and right auxiliary arrays is eliminated
"""

from typing import List


class Solution:
    def init_arr(self, size):
        # init an array of given size with all elements set to 1
        return [1 for _ in range(size)]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = self.init_arr(n)
        right = self.init_arr(n)
        product = self.init_arr(n)

        # left[i] = product of all integers to the left of i (EXCLUDING i)
        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]

        # right[i] = product of all integers to the right of i (EXCLUDING i)
        for i in range(n - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        # product[i] = product of all integers to the left of i times product of all integers to right of i
        for i in range(n):
            product[i] = left[i] * right[i]

        return product
