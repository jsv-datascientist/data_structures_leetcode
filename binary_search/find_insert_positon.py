
def search_insert(nums, target):
    nums.append(float('inf'))  # append an infinite element to handle edge case
    left, right = 0, len(nums)
    while right - left > 1:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid
    return left
