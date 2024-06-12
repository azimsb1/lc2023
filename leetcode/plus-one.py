"""
LC: https://leetcode.com/problems/plus-one/

Approach 1
----------
- approach inspired by the solution to add two (linked) lists problem
- maintain a carry
- for each digit:
    * add carry
    * update to the new digit
    * update carry

- since we're only incrementing by 1, max sum would be 10, so carry could be 0 or 1 (not greater)
- after repeating this process for all digits, in the reverse order, check at the end if carry is 1
    * if it is 1, add a new digit (1) to the beginning of the list
- return the (in-place) updated new list

Time complexity: O(n)
- where n = number of digits

Space complexity: O(1)
- since the algorithm updates the list in place

Approach 2
----------
- very similar to the first approach
- but do not need to maintain "carry"
- this is because, we know the following:
    * sum will be at most 10
    * the new digit will be (d+1) if d < 9, and will be 0 if d == 9

- in the reverse order, change 9s to 0s, until not 9 is seen
- when not 9 is seen, increment it and return
- in the case where reached start of the list:
    * this means not 9 not seen from the end to the start
    * so add digit 1 to the beginning of the list

Time complexity: still O(n)
- where n = number of digits
- visiting each digit once, and doing constant amount of work (flipping the number)
- in the worst case, if we need to insert 1 at index 0, all digits will move to the right by 1 unit, which is O(n)
- in this case, it will cost O(2n) which results ot O(n)

Space complexity: O(1)
- in place algorithm

Note:
* space complexity will be O(n) for both solutions if original list needs to be maintained a new one has to be created
* but based on the description of the question, we're assuming that the algorithm must do this in-place.
"""


# def plusOne(self, digits: List[int]) -> List[int]:
#     # at each iteration, should we add 1?
#     # carry can have only two values: 0 or 1
#     # carry is initially 1 because we need to initially increment
#     carry = 1
    
#     # iterate over each digit in reverse order
#     for i in range(len(digits)-1, -1, -1):
#         # add carry (which is 1) to the digit
#         sum = digits[i] + carry
#         # math trick:
#         # if digits[i] < 9, digits[i] will remain single digit and early exit
#         # if digits[i] == 9, digits[i] will become 0 and carry will be 1
#         digits[i] = sum % 10
#         carry = sum // 10

#         # early exit if nothing needs to be carried
#         if carry == 0:
#             return digits
    
#     # if reached here, means carry is still 1
#     # so insert 1 add the beginning of the array
#     digits.insert(0, 1)

#     # return the updated array
#     return digits


# Same runtime and approach as above, but simpler code
def plusOne(self, digits: List[int]) -> List[int]:
    # iterate over the digits in reverse order
    for i in range(len(digits)-1, -1, -1):
        # if 9, change to 0
        if digits[i] == 9:
            digits[i] = 0
        # if not 9, increment digit, and return
        else:
            digits[i] += 1
            return digits
    
    # reached here means only 9s so far, so add 1 to the beginning
    digits.insert(0, 1)

    return digits
