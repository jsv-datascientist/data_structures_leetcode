"""
 determine x when 
f(x)=50 for the function f(x)=x**4− x**2−10 for interval [−5,5).
"""

# Python program to find the root of a given function using Binary Search
import numpy as np

# Define a continuous function 'f' where f(x) = x^4 - x^2 - 10
def f(x):
    return x**4 - x**2 - 10

# Define the binary search function 
def binary_search(func, target, left, right, precision):
    middle = (left + right) / 2
    while  np.abs(func(middle) - target) > precision:
        if  target < func(middle):
            right = middle
        else:
            left = middle
        middle = (left + right) / 2
        
            
    return middle

epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 50  # target value for root of function 'f'
start = -5  # starting point of the interval
end = 5  # ending point of the interval

result = binary_search(f, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 50 within the interval [" + str(start) + ", " + str(end) + "] is: ", result)