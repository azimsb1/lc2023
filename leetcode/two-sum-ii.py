"""
LC: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
YT: https://www.youtube.com/watch?v=XKu_SEDAykw

Approach:
- since the input is sorted, we will use a two pointer approach
- for each iteration:
  * if sum of two numbers is target, return their indices
  * if sum is smaller, move left pointer one step forward (to increase the sum)
  * if the sum is bigger, move right pointer one step backwards (to decrease the sum)

Time complexity: O(n)
- where n = length of input array
- single pass, with two pointers

Space complexity: O(1)
- no additional auxiliary space
"""


def twoSum(self, numbers: List[int], target: int) -> List[int]:
  # two pointers
  left, right = 0, len(numbers) - 1

  # while the two pointers meet
  while left < right:
      # find sum of numbers at these pointers
      sum = numbers[left] + numbers[right]
      # found the target
      if sum == target:
          return [left+1, right+1]
      # sum is smaller than target, so try to increase the sum
      if sum < target:
          left += 1
      # sum is bigger than target, so try to reduce the sum
      else:
          right -= 1

  # no solution is found
  return [-1,-1] 
