def factorial(num):
    if num < 0:        # negative → return None (triggers 'Error')
        return None
    if num == 0:       # base case
        return 1
    return num * factorial(num - 1)


def factorials(nums):
    results = []
    for num in nums:
        f = factorial(num)
        if f is not None:
            results.append(f)
        else:
            results.append('Error')
    return results


print(factorials([2, 3, 4]))  # Should print: [2, 6, 24]
print(factorials([1, 5, 6]))  # Should print: [1, 120, 720]
print(factorials([0, -3, 10]))  # Should print: [1, 'Error', 3628800]