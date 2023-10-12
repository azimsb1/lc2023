"""
YT: https://www.youtube.com/watch?v=N0JkzO0mL9o

Given a sequence of integers as an array, determind whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Example: for `sequence = [1, 3, 2, 1]`, the output should be `False`. There is no one element in this array that can be removed in order to get a strictly increasing sequence.

Approach:
- keep a count of equal or decreasing trend
- check every element cur to it's previous element
- when there is a decrease:
  - check if count is more than 1. If it is, return False because only 1 element can be removed
  - if count is less than one, increment the count and check the following:
  1. can the previous element be removed and the sequence is strictly increasing, OR
  2. can the current element be removed and the sequence is strictly increasing

- for (1), nums[i] must be greater than nums[i-2]
- for (2), nums[i+1] must be greater than nums[i-1]
- if both are false, then return False as only removing one element is not sufficient to make the sequence strictly increasing
"""

def almost_increasing_sequence(sequence):
  # number of decreasing trends
  count_decreasing = 0

  # check each number to its previous number
  for i in range(1, len(sequence)):
    # decreasing pattern
    if sequence[i] <= sequence[i-1]:
      # increment the counter
      count_decreasing += 1
      # not the first time a decreasing trend is found, return False
      if count_decreasing > 1:
        return False
      # 1. remove the previous element
      choice_one = sequence[i] > sequence[i-2]
      # 2. remove the current element
      choice_two = sequence[i+1] > sequence[i-1]
      # at least one needs to be true to continue
      if not choice_one and not choice_two:
        return False
        
  # if reached here, that means no problems
  return True


# TODO: write test cases or unit tests
