"""
LC: https://leetcode.com/problems/top-k-frequent-elements/

Approach:
- note: this approach is called bucket sort

- we will create an array, where each index represents the different frequencies of the numbers
- and each element will be a list of numbers that appear _that_ many times
- to clarify, arr[i] = the list of numbers that appear i times

- to know how many times each number appears, we will store num,freq in a hashmap

- finally, we will look at the array from the end, since we want _more_ frequent elements _first_
- keep picking the elements from the end to the start, until we get `k` elements

Time complexity: O(n)
- where n = length of nums
- each sub section of the algorithm runs in linear time:
  * a. we count the frequencies
  * b. we place elements in the respective buckets
  * c. we loop through the buckets from the end, picking k elements, n at worst case when k = n

Space complexity: O(n)
- where n = length of nums
- in the worst case when the same number appears let's say 10 times, the size of the arr will be 11, with a single number appearing in a list at the last index
"""


# this function maps each number to its frequency
def make_freq_map(nums):
    # this is the same as looping through nums and incrementing counter by 1
    return Counter(nums)


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # maps each number and how many times it appears in the input
    freq_map = make_freq_map(nums)

    # freq_arr[i] = the list of numbers that appear i times
    freq_arr = [[] for _ in range(len(nums) + 1)]
    
    # for each number, check its frequency
    # and store it at the index which equals its frequence
    for num, freq in freq_map.items():
        freq_arr[freq].append(num)
    
    # poupulate this list with the top k frequent elements and return it
    result = []

    # loop from the end, because we want more frequent first
    for i in range(len(freq_arr) - 1, -1, -1):
        # i = certain frequency; which elements appear i times?
        for num in freq_arr[i]:
            # add the number to the result
            result.append(num)
            # end and return if we have populated k numbers
            if len(result) == k:
                return result
