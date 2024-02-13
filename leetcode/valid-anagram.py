"""
LC: https://leetcode.com/problems/valid-anagram

Time complexity: O(a+b)
Space complexity: O(a+b)

where a is the length of string s,
  and b is the length of string t.
"""


from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if lengths are different, can't be anagrams
        if len(s) != len(t):
            return False

        # dict will count the freq of chars in s and t
        count = defaultdict(int)

        # for each char in s, increment the count
        for char in s:
            count[char] += 1
        
        # for each char in t, decrement the count
        for char in t:
            count[char] -= 1
        
        # if all counts are 0, that means same characters and frequencies
        for val in count.values():
            if val != 0:
                return False
        return True


solution = Solution()
assert(solution.isAnagram('racecar', 'carrace') == True)
