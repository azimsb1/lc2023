"""
Question: Given an array of integers, find the two elements whose sum is closes to 0.

GfG: https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
YT: https://www.youtube.com/watch?v=HUwYrtrOcd0

Approach 1: Brute force
- look at every pair, find the absolute sum
- if the absolute sum is smaller than min abs sum, update the two numbers
- time complexity: O(n^2), space complexity: O(1)

Approach 2: Optimized, 2-pointer approach
- sort the array
- use two pointers, l and r, from the two ends of the array
- find the absolute sum, and update the min abs sum if necessary
- if the sum is < 0, move l pointer to the right (to bring it closer to 0)
- if the sum is > 0, move r pointer to the left  (to bring it closer to 0)
- do this until l and r pointers meet

Time complexity: O(n log n)
- O(n log n) to sort the input array
- O(n) for the two pointer single traversal
- O(n log n) + O(n) = O(n log n)

Space complexity: O(n)
- creating a copy of the input array, and sorting it
- assumption: not modifying the original input array
"""

def pair_sum_closes_to_zero(input_arr):
    # edge case
    if len(input_arr) < 2:
        return [-1, -1]
    
    # create a copy of the input_arr and sort it
    sorted_arr = input_arr[:]
    sorted_arr.sort()

    # min_abs_sum tracks the smallest (absolute) sum 
    # l and r min track the indices of the elements that had that sum
    min_abs_sum, l_min , r_min = None, None, None

    # two pointers
    l, r = 0, len(sorted_arr) - 1
    # while pointers meet
    while l != r:
        # find the sum
        pair_sum = sorted_arr[l] + sorted_arr[r]

        # if sum is smaller than min_abs_sum, update minimums
        if not min_abs_sum or abs(pair_sum) < min_abs_sum:
            min_abs_sum = abs(pair_sum)
            l_min, r_min = l, r

        # move closer to 0
        if pair_sum <= 0:
            l += 1
        else:
            r -=1
    
    # return the two numbers that summed to the min abs sum
    return [sorted_arr[l_min], sorted_arr[r_min]]


input_arr = [1, 60, -10, 70, -80, 101, 85]
expected_arr = [-80, 85]
assert(pair_sum_closes_to_zero(input_arr) == expected_arr)
