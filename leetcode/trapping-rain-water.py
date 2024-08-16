'''
LC: https://leetcode.com/problems/trapping-rain-water/

Approach:
- key insight: water trapped at each index must reach an equilibrium determined by the tallest buildings (or bars) on either side.
- simplify the problem by breaking it down:
  * how much water each individual index (or building) can hold?

- for any given index, the amount of water it can hold depends on the tallest building to its left and the tallest building to its right
- water level at that index is determined by the shorter of these two heights, minus the height of the building at that index.

- we maintain two auxiliary arrays:
  * max_left: Stores the tallest building to the left of each index.
  * max_right: Stores the tallest building to the right of each index.

- water trapped at each index by using the formula `water[i] = min(max_left[i], max_right[i]) - height[i])`

Time complexity O(n):
- where n = length of input arr.
- generating max_to_left and max_to_right takes O(n) time each.
- calculating the total trapped water also takes O(n) time.
- so, the overall time complexity is O(n).

Space complexity: O(n):
- where n = length of input arr.
- two aux arrays, each of size n.
- the space complexity is O(n).

note: there is a more space-efficient two-pointer approach available on LeetCode,
that achieves O(1) space complexity while maintaining O(N) time complexity.
'''

def trap(height: List[int]) -> int:
      n = len(height)
      max_left = [0 for _ in range(n)]
      max_right = [0 for _ in range(n)]

      for i in range(1, n):
          max_left[i] = max(max_left[i-1], height[i-1])
      
      for i in range(n-2, -1, -1):
          max_right[i] = max(max_right[i+1], height[i+1])
      
      total_water = 0
      for i in range(n):
          water = min(max_left[i], max_right[i]) - height[i]
          total_water += max(0, water)
      
      return total_water
