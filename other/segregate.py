"""
Companies: Capital One

Custom question: segregate odd and even numbers in an array .
Odd numbers must appear first, followed by even.

YT: https://www.youtube.com/watch?v=5ah-f1NlE_w

Approach:
- two pointers starting from the left and right corners
- left keeps odd numbers and right keeps odd numbers

- in each iteration:
    * if left is already at odd, just increment it
    * if left is at even but so is right, decrement right (to potentially find for an odd number to its left)
    * otherwise, it means that left is at even and right is at odd, so swap them and move them both

Time complexity: O(n)
- where n = number of elements in the array
- two pointer approach until they meet

Space complexity: O(1)
- doing this in place, so aux space required
"""


def odd(num):
    # a number is odd if when divided by 2 the remainder is not 0
    return num%2 != 0


def even(num):
    # a number is even if the remainder is 0 when divided by 2
    return num%2 == 0


# main function starts here
def segregate(arr):
    left, right = 0, len(arr) - 1

    # while two pointers meet
    while left < right:
        # left already sits at odd
        if odd(arr[left]):
            # increment left
            left += 1
    
        # left sits at even but right also sits at even
        elif even(arr[left]) and even(arr[right]):
            # decrement right
            right -= 1
        
        # left sits at even and right sits at odd
        else:
            # swap elements at left and right
            arr[left], arr[right] = arr[right], arr[left]
            # move both
            left += 1 ; right -= 1


input_arr = [2, 5, 3, 7, 8, 10, 12, 13]
expected_arr = [13, 5, 3, 7, 8, 10, 12, 2]
segregate(input_arr)
assert(input_arr == expected_arr)


input_arr = [2, 4, 1, 6, 3, 8, 7]
expected_arr = [7, 3, 1, 6, 4, 8, 2]
segregate(input_arr)
assert(input_arr == expected_arr)
