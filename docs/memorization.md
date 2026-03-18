```

fibonanci 
Naive Recusion is O(2ⁿ)
fib(5)
├── fib(4)
│   ├── fib(3)        ← calculated again!
│   │   ├── fib(2)    ← calculated again!
│   │   └── fib(1)
│   └── fib(2)        ← calculated again!
└── fib(3)            ← repeated!
    ├── fib(2)        ← repeated!
    └── fib(1)

Problem 1: Efficient Approach Explanation
Beyond handling base cases in the naive solution (n≤1), we integrate an optimization technique known as memoization to further enhance the function. With memoization, we store the results of previous Fibonacci number calculations. This way, for any given input n, if we've already calculated the Fibonacci number for n, there's no need to recalculate; the function can directly return the stored result.

This combination of addressing base cases and leveraging memoization avoids unnecessary repetitions and improves the function's efficiency, particularly for larger inputs.


def fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n - 1, computed) + fib(n - 2, computed)
    return computed[n]


In this function, we use a Python dictionary computed to store the Fibonacci numbers we've computed so far. 
If a number n is not in the dictionary computed, we calculate it using the recursive formula and store the result in our dictionary. If the number n is already in our dictionary, we simply return the value, thus avoiding the computation. 
Edge cases results (n = 0 and n = 1) are stored in the computed list by default.

This function now computes the nth Fibonacci number in linear time O(n), which is a significant improvement 
over the naive recursive implementation. Each number is calculated only once, and the function can handle
 a large n efficien


 SUM in array 
 ===========

 arr = [3, 1, 4, 1, 5]

# sum from index 1 to 3 → adds 1 + 4 + 1 every time
# sum from index 0 to 3 → adds 3 + 1 + 4 + 1 every time
# repeating work!
```

**The manuscript analogy:**
```
Pages:     [3,  1,  4,  1,  5]
           pg1 pg2 pg3 pg4 pg5

Instead of re-counting pages 1-3 every time, you keep a running total:
Build prefix sum once:
arr    = [3,  1,  4,  1,  5]
prefix = [3,  4,  8,  9,  14]
#         3  3+1 4+4 8+1 9+5

Now any range sum is just one subtraction:

# sum from index 1 to 3?
prefix[3] - prefix[0]  # 9 - 3 = 7  ✅ (1 + 4 + 1)

# sum from index 0 to 2?
prefix[2]              # 8           ✅ (3 + 1 + 4)

# sum from index 2 to 4?
prefix[4] - prefix[1]  # 14 - 4 = 10 ✅ (4 + 1 + 5)

def build_prefix(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix

def range_sum(prefix, left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left-1]


OR 
def arraySum(arr):
    return arr[0] + arraySum(arr[1:])

# fib([3,1,4,1,5])
# arr[1:] → [1,4,1,5]  ← new array in memory
# arr[1:] → [4,1,5]    ← new array in memory
# arr[1:] → [1,5]      ← new array in memory
# arr[1:] → [5]        ← new array in memory



def arraySum(arr, index=0): 
   if index == len(arr): 
       return 0 
   else:
       return arr[index] + arraySum(arr, index + 1)
# arraySum([3,1,4,1,5], 0)
# arraySum([3,1,4,1,5], 1)  ← same array!
# arraySum([3,1,4,1,5], 2)  ← same array!
# arraySum([3,1,4,1,5], 3)  ← same array!
# arraySum([3,1,4,1,5], 4)  ← same array!


arraySum([3,1,4,1,5], 0)
= arr[0] + arraySum([3,1,4,1,5], 1)   # 3 + ...
= arr[0] + arr[1] + arraySum(..., 2)   # 3 + 1 + ...
= arr[0] + arr[1] + arr[2] + arraySum(..., 3)   # 3 + 1 + 4 + ...
= arr[0] + arr[1] + arr[2] + arr[3] + arraySum(..., 4)   # 3 + 1 + 4 + 1 + ...
= arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arraySum(..., 5)  # 3+1+4+1+5+...
= 3 + 1 + 4 + 1 + 5 + 0   # index == len(arr), return 0
= 14

Why index instead of slicing:
Approach                  Code                     Space
======================================================================================
Slicing                  arraySum(arr[1:])         O(n) — creates new array each call
Index                    arraySum(arr, index+1)    O(1) — same array, just moves pointer
```



```
Calculating Factorial

n!=n⋅(n−1)⋅(n−2)⋅...⋅2⋅1.
treks (when calculating the number of ways to traverse a path), and 
even poker games (when calculating the number of ways to arrange cards).

 

5! as 
5⋅4!,
4⋅3! 
until 1! or 0!

def factorial(n): 
   if n == 0 or n == 1: 
       return 1
   else:
       return n * factorial(n - 1)
```