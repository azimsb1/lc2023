"""
Custom question: segregate odd and even numbers in an array in a sorted order.
Odd numbers must appear first, followed by even.
"""

def odd(num):
    return num%2 != 0

def even(num):
    return num%2 == 0

def segregate(arr):
    i = 0 ; j = 1
    while j < len(arr):
        # if i sits at even and j sits at odd
        if even(arr[i]) and odd(arr[j]):
            # swap
            arr[i], arr[j] = arr[j], arr[i]
            # acheived what we want - increment both pointers
            i += 1 ; j += 1
        
        # if i sits at odd and j sits at even
        elif odd(arr[i]) and even(arr[j]):
            # already what we want - increment both pointers
            i += 1 ; j += 1
            

        # if i and j sit at odd
        elif odd(arr[i]) and odd(arr[j]):
            # i is already at odd, so increment i
            i += 1
        
        # if i and j sit at even
        else:
            # increment j so we can find an odd number for i
            j += 1
    
    return arr


def sorted_segregate(arr):
    arr.sort()
    segregate(arr)

input_arr = [2, 5, -3, 7, -8, 10, 12, 13]
expected_arr = [-3, 5, 7, 13, -8, 2, 10, 12]
sorted_segregate(input_arr)
print("arr: ", input_arr)
assert(input_arr == expected_arr)


"""

-3 5 2 -8 7 10 12 13

      i   j

"""
