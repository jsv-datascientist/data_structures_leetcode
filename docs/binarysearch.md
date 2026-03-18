```
binary search
Binary Search is a search algorithm operating on a sorted list or array. 

- divide 
_ search in left , if found skip right else keep doing 

imagine you have a sorted list of numbers as: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], and you've been tasked with determining if the number 3 is present in the list. With Binary Search, it directly jumps to the middle. If the number is equal to the middle element, our search is complete. But if the number is smaller than the middle element, Binary Search discards the second half of the list and continues the search only on the first half. This process is repeated until the number is found.

Binary Search Algorithm
=========================
Binary search uses a divide-and-conquer approach to find a specific element in a list. Regarding time complexity, this algorithm accomplishes the task in the order of O(logn), making it a preferable choice for large datasets.

The steps involved in the binary search algorithm are as follows:

- Calculate the middle index = (lowest index + the highest index) / 2.

-  target < data[mid]:, move left.

- target > data[mid]:, move right.

Once finished, check if data[left] equals target - if yes, we found the target element; if not - target doesn't exist in the data array.

O(logn). This logarithmic time behavior makes binary search ideal for large datasets. This is because, with each comparison, binary search eliminates half of the elements, reducing the search time exponentially.

 space complexity 
- O(1) as it only uses a fixed amount of space to store the data
- recursive version has higher space complexity — O(logn) — since it uses additional space in the form of a call stack during recursive tasks.

```



```
Search in rotated list 
[7, 8, 9, 2, 3, 4]

This list was sorted from 2 to 9
Find number 4, it is in right half
```



```
Apply on continous function 

 Well, the mechanism of binary search remains much the same, but instead of comparing the middle element to the target, we compare the middle point x's function value f(x) to the target. We continuously narrow down an interval until we reach an interval small enough that the function value within it is as close to the target as we demand.

 The smaller the 
ϵ
ϵ, the higher the precision of our target value since we are narrowing down the interval width to a smaller range. However, this comes with a trade-off. A smaller 
ϵ
ϵ means that our while loop will run more times, and thus, the algorithm will take longer to reach the desired precision level
```

```
Rotated Array 

[1, 2, 4, 5, 8, 9, 11, 15], but after rotaing [8, 9, 11, 15, 1, 2, 4, 5].
a logarithmic time complexity of O(logn)

Midpoint value is equal to the target - our job is done, return the midpoint.
Both the target and midpoint are in the first half of the array (before the rotation point) - the target lies within the left half (from left to mid - 1).

To check whether both the target and midpoint lie in the first half, we check that nums[left] <= nums[mid] and nums[left] <= target < nums[mid].

The target and midpoint are in the second half (after the rotation point) - the target lies within the right half (mid + 1 to right).

To check whether both the target and midpoint lie in the second half, we check that nums[mid] <= nums[right] and nums[mid] < target <= nums[right].

The midpoint falls into the first half while the target is in the second half - the target is located in the right half.

To check whether the midpoint falls into the first half and the target falls into the second half, we check that nums[mid] > nums[right] (the target can't fall into the first half anymore, as this scenario is covered in case 3).

Otherwise, the midpoint falls into the second half, and the target lies in the first - our target should be in the left half.

Problem 2: Locate the First and Last Position of an Element in a Sorted Array
finding both the first and last positions of a certain target value in a sorted array. If the target is not found within the array, your function should return [-1, -1]c

a situation involving time-series analysis. For instance, you have a sorted array filled with timestamps of user activities. A user could perform the same activity multiple times, and your task is to determine the first and last instance that a particular activity was performed.


Problem 3: Find or Define Insert Position in a Sorted List
ocument management system where reports are sorted based on their IDs. Suppose a new report comes in, and it has to be placed in the correct position based on its ID. Here, our task mirrors the system's behavior - placing a number correctly in a sorted list.
```