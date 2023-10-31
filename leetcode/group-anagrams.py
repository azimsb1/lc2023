"""
LC: https://leetcode.com/problems/group-anagrams/
YT: https://www.youtube.com/watch?v=vzdNOK2oB2E

Approach:
- key observation is that a given set of strings are anagrams if they have the _same_ number of _same_ characters
_ for each string, let's calculate the frequency of all characters that appear and store this
- we _cannot_ store these frequencies in a dict (ex: {'a':0, 'b':3, ...}) or a list (ex: [0, 3, ...]) because:
  * dict and lists are unhashable
  * hashing them is important because when we group strings in a hashmap, the frequency count datastructure will be the key
  * so, we make tuples of frequency counts to group these strings

Time complexity: O(n * s)
- where:
  * s = avergae len of string
  * n = total number of strings
- for each string n, we look at each of its characters
- so the time complexity is O(n * s)

Space complexity: O(n)
- where n = total number of strings
"""


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # map of char counts of each string to the list of anagrams
    groups = defaultdict(list)

    # for each string
    for str in strs:
        # [freq_a, freq_b, ... , freq_z]
        freq = [0 for _ in range(26)]
        # for each char in the string
        for char in str:
            # use ascii values to find index of the char
            # such that a:0, ... , z:25
            index = ord(char) - ord('a')
            
            # increment the freq of that char
            freq[index] += 1

        # store the char frequencies list as a tuple in the hashmap
        freq_tuple = tuple(freq)
        # add string to the list of strings for that tuple
        groups[freq_tuple].append(str)

    # return the map's values which are groups of anagrams
    return groups.values()
