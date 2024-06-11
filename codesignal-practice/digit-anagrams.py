'''
Given an array of integers `a`, your task is to count the number of pairs `i` and `j` (where 0 ≤ i < j < a.length), such that `a[i]` and `a[j]` are **digit anagrams**.
Two integers are considered to be digit anagrams if they contain the same digits. In other words, one can be obtained from the other by rearranging the digits (or trivially, if the numbers are equal). For example, `54275` and `45572` are digit anagrams, but `321` and `782` are not (since they don't contain the same digits). `220` and `22` are also not considered as digit anagrams, since they don't even have the same number of digits.

Example

For `a = [25, 35, 872, 228, 53, 278, 872]`, the output should be `solution(a) = 4.`.

There are 4 pairs of digit anagrams:
* `a[1] = 35 and a[4] = 53 (i = 1 and j = 4)`,
* `a[2] = 872 and a[5] = 278 (i = 2 and j = 5)`,
* `a[2] = 872 and a[6] = 872 (i = 2 and j = 6)`,
* `a[5] = 278 and a[6] = 872 (i = 5 and j = 6)`.

Input/Output
* [execution time limit] 6 seconds (py3)
* [memory limit] 1 GB
* [input] array.integer a
  An array of non-negative integers.
  Guaranteed constraints:
  1 ≤ a.length ≤ 105,
  0 ≤ a[i] ≤ 109.
* [output] integer64
The number of pairs i and j, such that a[i] and a[j] are digit anagrams.
'''

'''
# Brute force

from collections import defaultdict

def digit_anagrams(n1, n2):
  # if numbers are same, they are anagrams
  if n1 == n2:
  return True
  # if different lengths, not anagrams
  # return False
  # all digits and their frequencies must match to be anagrams
  count = defaultdict(int)

  while n1 > 0:
    digit = n1 % 10
    count[digit] += 1
    n1 = n1//10

  while n2 > 0:
    digit = n2 % 10
    if digit not in count:
      return False

    count[digit] -= 1

    if count[digit] == 0:
      del count[digit]
    n2 = n2//10

  if len(count) != 0:
    return False
  
  return True



def solution(a):
  anagrams = 0

  for i in range(len(a)-1):
    for j in range(i+1, len(a)):
      if digit_anagrams(a[i], a[j]):
        anagrams += 1
 return anagrams
'''


# Optimized

from collections import defaultdict

def solution(a):
  count = defaultdict(int)
  for number in a:
    num_str = ''.join(sorted(str(number)))
    count[num_str] += 1


  anagrams = 0
  for freq in count.values():
    anagrams += (freq * (freq-1))/2

  return anagrams
