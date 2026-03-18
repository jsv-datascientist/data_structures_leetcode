def quick_sort(arr):
    if len(arr) <= 1:
        # if the array contains 0 or 1 element, it's already sorted
        return arr
    pivot = arr[len(arr) // 2] # select a pivot as a middle element
    left = [x for x in arr if x < pivot] # elements less than `pivot`
    middle = [x for x in arr if x == pivot] # elements equal to `pivot`
    right = [x for x in arr if x > pivot] # elements larger than `pivot`
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([9, 7, 5, 11, 12, 2, 14, 3, 10, 6]))

# Outputs: [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]

import random

pivot = arr[random.randint(0, len(arr) - 1)]

"""
Space complexity refers to the amount of memory an algorithm needs to complete its run. 
With Quick Sort, the space complexity stems primarily from its recursive nature. 
Each recursive call requires additional space on the call stack, proportional to the depth of recursion However,
Quick Sort averages an excellent space complexity of 
O(logn).

It is possible to implement quick sort without using recursion; in that case, the additional space complexity will be 
O(1).
"""