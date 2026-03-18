

"""
An inversion = a pair (i, j) where:
  i < j  BUT  arr[i] > arr[j]
  ↑ left       ↑ left is BIGGER than right
  comes first  comes after

In other words: two elements that are OUT OF ORDER.

arr = [5, 4, 3, 2, 1]

Every pair is an inversion:
(5,4), (5,3), (5,2), (5,1)   ← 4 inversions from 5
(4,3), (4,2), (4,1)           ← 3 inversions from 4
(3,2), (3,1)                  ← 2 inversions from 3
(2,1)                         ← 1 inversion  from 2

Total = 4+3+2+1 = 10 inversions

Real world framing:
"Given a stream of log timestamps, some arrived
 out of order. Count how many out-of-order pairs exist
 to measure how scrambled the stream is."

[1, 3, 2, 4] → 1 inversion  → slightly scrambled
[5, 4, 3, 2, 1] → 10 inversions → completely reversed

def count_inversions_brute(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):   # every pair
            if arr[i] > arr[j]:   # out of order?
                count += 1
return count
Works but O(n²) — too slow for large log streams.


LOGIC 
In other words:
When right[j] < left[i]:
  right[j] is out of order with ALL remaining left elements
  → count them ALL at once → O(1) per such event
  
  inversion += len(left)-1

"""


def count_inversion(arr):
    
    if len(arr) <= 1:
        return arr,0
    
    mid = len(arr) // 2
    
    left, left_inv = count_inversion(arr[:mid])
    right, right_inv = count_inversion(arr[mid:])
    
    merged, inversion = merge_sort(left,right)
    
    return merged, inversion + left_inv + right_inv

def merge_sort(left, right):
    result = []
    inversion = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            
            inversion += len(left) - i
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    return result, inversion


if __name__ == "__main__":
    arr = [3, 1, 4, 2]
    sorted_arr, total = count_inversion(arr)
    print(f"Actual: {arr}")
    print(f"Inversions: {total}")      # 3
    print(f"Sorted: {sorted_arr}")  