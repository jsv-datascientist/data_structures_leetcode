
"""
Locate the First and Last Position of an Element in a Sorted Array
"""
def get_first_last_pos(nums, target):
    def binary_search(left, right, find_first):
        if left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (find_first and target == nums[mid]):
                return binary_search(left, mid - 1, find_first)
            else:
                return binary_search(mid + 1, right, find_first)
        return left

    first = binary_search(0, len(nums) - 1, True)
    last = binary_search(0, len(nums) - 1, False) - 1
    if first <= last:
        return [first, last]
    else:
        return [-1, -1]