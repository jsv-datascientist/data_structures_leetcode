"""
 Consider the continuous function 
f(x)=x2−2, and let's try to find x for which f(x)=0, within the interval [1, 2].

Why target is 0, at ground momentim the height is 0
"""

# Define the function
def f(x):
    return x * x - 2

# Define the binary search function 
def binary_search(target, left, right, precision):
    while right - left > precision:
        mid = (left + right) / 2
        if f(mid) < target: # If the midpoint value is less than the target...
            left = mid  # ...update the left boundary to be the midpoint.
        else:
            right = mid  # Otherwise, update the right boundary.
    return left # Return the left boundary of our final, narrow interval.

epsilon = 1e-6
result = binary_search(0, 1, 2, epsilon)
print("x for which f(x) is approximately 0:", result)

# Outputs:
# x for which f(x) is approximately 0: 1.4142131805419922