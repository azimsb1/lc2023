"""
LC: https://leetcode.com/problems/longest-increasing-subsequence/
* YT: https://www.youtube.com/watch?v=fV-TF4OvZpk 

Approach 1: Brute Force O(2^n)
- generate all subsequences
- validate increasing subsequence property
- find the longest from the validated ones
- time complexiy is exponential

Approach 2: Dynamic Programming (Optimal)
- we create a dynamic programming array of size len(nums)
- each cell represents the answer to the subproblem for
  the subsequence from index 0 to index i (including the element at index i).
- i.e. subproblem at i = length of longest increasing subsequence for array nums[:i+1]

Time complexity: O(n^2)
- where n = len(nums)
- for each of the n elements, we solve the LIS problem which takes O(n) time
- therefore we yield a O( n^2 ) runtime complexity

Space complexity: O(n)
- storing the answer to each of the n LIS subproblems
"""

def lengthOfLIS(nums: List[int]) -> int:
  # dp_arr[i] = solution for subproblem for nums[:i+1]
  dp_arr = [1 for _ in range(len(nums))]

  # find solution for each subproblem
  for j in range(1, len(nums)):
      # can the current element be extended at any of the indices before it
      for i in range(j):
          # if current element is bigger, the subsequence can be extended 
          if nums[j] > nums[i]:
              # optimal solution is max of:
              # current max and solution to the subproblem plus 1 (extension of current element)
              dp_arr[j] = max(dp_arr[j], dp_arr[i] + 1)
  
  # max of all subproblems is the best subproblem / subsequence
  return max(dp_arr)
