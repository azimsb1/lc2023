"""
LC: https://leetcode.com/problems/subarray-sum-equals-k/
YT: https://www.youtube.com/watch?v=fFVZt-6sgyo

Approach 1 (Brute Force) -- O(n^2):
- explore all sub arrays, and keep a running sum for each subarray
- everytime a new number is added to the window (subarray), increase the running sum and compare with k
- since window's l will go from 0...n-2 and for each of these l, we will have an r from l...n-1, this solution will take O(n^2) time

Approach 2 (Optimized) -- Prefix Sum:
- for the current window and its running sum, is there a prefix array that can be chopped off such that the remaining subarray's sum equals k?
- so, for each window, check if there is a complement
- complement is a prefix subarray sum such that running_sum - this prefix subarray sum = k
- this is similar to 2sum, but instead of dealing with numbers, we are dealing with sums (of subarrays)
- in summary, for each running_sum, check if map contains running_sum - k
- note that a map is used because there could be multiple prefix subarrays with that sum (since we are dealing with -ve numbers as well)

Time complexity -- O(n):
- one pass
- where n = len(nums)

Space complexity -- O(n):
- storing prefix sums as we iterate over nums
"""


def subarraySum(nums: List[int], k: int) -> int:
  # track and return number of subarrays
  ans = 0

  # keeps track of sums of subarrays
  prefix_sum = defaultdict(int)
  # this is default, as [] has sum of 0
  prefix_sum[0] = 1

  # keeps track of sum of the window
  running_sum = 0
  # one pass
  for num in nums:
      # update the sum of the window
      running_sum += num
      # complement is a number which when removed from running_sum gives k
      complement = running_sum - k
      # does a subarray with sum complement exist
      if complement in prefix_sum:
          # how many such subarrays are there
          ans += prefix_sum[complement]
      # save this prefix sum for later
      prefix_sum[running_sum] += 1

  # number of windows or subarrays whose sum equal k
  return ans
