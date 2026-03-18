
def binary_search_iterative(data, target):
    # We will search in the interval [low, high), where the right border is excluded
    low = 0
    high = len(data)

    while high - low > 1: # search until the length of the interval > 1
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid # Continue our search in [low, mid)
        else:
            low = mid # Continue our search in [mid, high)
    return low if data[low] == target else None

def binary_search_recursive(data, target, low, high):
    if high - low <= 1:
        return low if data[low] == target else None
    mid = (low + high) // 2
    if target < data[mid]:
        return binary_search_recursive(data, target, low, mid)
    else:
        return binary_search_recursive(data, target, mid, high)
    


def insert_position(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1

    return left

print(insert_position([1, 2, 3, 3, 5], 3))   # 2 ✅
print(insert_position([1, 2, 3, 3, 5], 4))   # 4 ✅
print(insert_position([1, 3, 5, 7, 9], 10))  # 5 ✅