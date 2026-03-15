Sorting 

## 1 — Bubble Sort

```

Repeatedly compare adjacent elements.
If left > right → swap.
Largest element "bubbles up" to the end each pass.

Time:
  Best:    O(n)    ← already sorted, with optimization
  Average: O(n²)   ← nested loops
  Worst:   O(n²)   ← reverse sorted

Space:    O(1)    ← sorts in place, no extra memory
Stable:   YES     ← equal elements keep original order

Honest answer: NEVER in production code.
O(n²) is too slow for any real data.


Pass 1:
[5, 3, 8, 1]
 ↑  ↑
 5 > 3 → swap
[3, 5, 8, 1]
    ↑  ↑
    5 < 8 → no swap
[3, 5, 8, 1]
       ↑  ↑
       8 > 1 → swap
[3, 5, 1, 8]  ← 8 bubbled to end ✅

Pass 2:
[3, 5, 1, 8]
 ↑  ↑
 3 < 5 → no swap
[3, 5, 1, 8]
    ↑  ↑
    5 > 1 → swap
[3, 1, 5, 8]  ← 5 bubbled to position ✅

Pass 3:
[3, 1, 5, 8]
 ↑  ↑
 3 > 1 → swap
[1, 3, 5, 8] ✅ sorted!
```
```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:      # no swaps = already sorted
            break            # stop early → best case O(n)
    return arr
```

 # 2 — Selection Sort
 ```
 The Idea

Find the MINIMUM element in the unsorted portion.
Swap it to the front.
Repeat for remaining unsorted portion.


Different from bubble sort:
Bubble sort:    swaps many times per pass
Selection sort: swaps ONCE per pass (minimum to front)

Pass 1: find min in [5, 3, 8, 1] = 1
        swap 1 with first element
        [1, 3, 8, 5]  ← 1 in correct place ✅
         ↑ sorted

Pass 2: find min in [3, 8, 5] = 3
        already in place, no swap
        [1, 3, 8, 5]  ← 3 in correct place ✅
            ↑ sorted

Pass 3: find min in [8, 5] = 5
        swap 5 with 8
        [1, 3, 5, 8]  ← 5 in correct place ✅

Done! [1, 3, 5, 8] ✅
 ```

 ```
 def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # find minimum in unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # swap minimum to front
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
```

---

## Complexity
```
Time:
  Best:    O(n²)  ← always scans full unsorted portion
  Average: O(n²)
  Worst:   O(n²)

Space:   O(1)   ← in place
Stable:  NO     ← swapping can change relative order
                   e.g. [3a, 3b, 1] → swap 1 with 3a
                   → [1, 3b, 3a] ← 3a and 3b order changed
```

---

## Bubble vs Selection — Side by Side
```
                Bubble Sort       Selection Sort
─────────────────────────────────────────────────
Swaps per pass  many              exactly ONE
Best case       O(n)              O(n²)
Worst case      O(n²)             O(n²)
Stable          YES               NO
When to use     nearly sorted     minimizing swaps
```

---

## When to Use at ORG
```
NEVER in production — O(n²) too slow.

But worth knowing:
✅ Useful when swap cost is HIGH
   (e.g. writing to disk — minimize writes)
✅ Shows understanding of in-place sorting
```

---

## The One Thing to Remember
```
Selection sort = find minimum, place at front
                ONE swap per pass
                always O(n²) — no best case improvement
                O(1) space, NOT stable
 ```


 
 # 2 — Insertion  Sort
 ```
 Idea 

 Build sorted portion one element at a time.
 Pick next element, INSERT it into correct position
 in the already-sorted left portion.

 Like sorting playing cards in your hand:
 Pick up card → slide it left until correct position

[5, 3, 8, 1]
 Start: sorted portion = [5], unsorted = [3, 8, 1]

Step 1: pick 3
        compare with sorted portion [5]
        3 < 5 → shift 5 right, insert 3
        [3, 5, 8, 1]
         ↑──┘ sorted

Step 2: pick 8
        compare with sorted portion [3, 5]
        8 > 5 → insert here
        [3, 5, 8, 1]
         ↑─────┘ sorted

Step 3: pick 1
        compare with sorted portion [3, 5, 8]
        1 < 8 → shift 8 right
        1 < 5 → shift 5 right
        1 < 3 → shift 3 right, insert 1
        [1, 3, 5, 8] ✅
 ```

 ```
 def insertion_sort(arr):
    for i in range(1, n):
        key = arr[i]          # element to insert
        j = i - 1             # start of sorted portion

        # shift elements right until correct position found
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # shift right
            j -= 1

        arr[j + 1] = key          # insert in correct position

    return arr
```

---

## Complexity
```
Time:
  Best:    O(n)    ← already sorted, inner while never runs
  Average: O(n²)
  Worst:   O(n²)   ← reverse sorted

Space:   O(1)   ← in place
Stable:  YES    ← equal elements keep original order
```

---

## Why Insertion Sort Matters at Datadog
```
1. Python's Timsort uses insertion sort for SMALL arrays (< 64 elements)
   → Timsort = merge sort + insertion sort combined

2. Best for nearly sorted data → O(n)
   → Log streams are often nearly sorted by timestamp!

3. Online algorithm — can sort as data arrives
   → Perfect for streaming data
```

---

## All 3 Simple Sorts — Comparison
```
                Bubble    Selection    Insertion
──────────────────────────────────────────────────
Best case       O(n)      O(n²)        O(n)
Average         O(n²)     O(n²)        O(n²)
Worst           O(n²)     O(n²)        O(n²)
Space           O(1)      O(1)         O(1)
Stable          YES       NO           YES
Good for        nearly    min swaps    nearly
                sorted    needed       sorted/streaming
 ```



 
 # 2 — Merge  Sort
 ```
 Perfect! ✅ All 3 correct.
Step 1: key=2 → shift 4 → insert 2 → [2, 4, 7, 1] ✅
Step 2: key=7 → 7>4, no shift       → [2, 4, 7, 1] ✅
Step 3: key=1 → shift 7,4,2 → insert 1 → [1, 2, 4, 7] ✅
Insertion sort locked. ✅

Sorting #4 — Merge Sort
The Idea
DIVIDE array in half recursively until size 1.
MERGE the halves back together in sorted order.

Divide until can't divide → then merge sorted pieces.

This is the first O(n log n) sort — significantly faster than O(n²).


DIVIDE phase:
        [5, 3, 8, 1]
           /      \
       [5, 3]    [8, 1]
       /    \    /    \
      [5]  [3] [8]   [1]
      ↑ base case — size 1, already sorted

MERGE phase:
      [5]  [3] [8]   [1]
       \    /    \    /
       [3, 5]   [1, 8]
           \      /
         [1, 3, 5, 8] ✅

Merge [3, 5] and [1, 8]:

left  = [3, 5]    i = 0
right = [1, 8]    j = 0
result = []

Compare left[0]=3 vs right[0]=1
  1 < 3 → take from right → result=[1], j=1

Compare left[0]=3 vs right[1]=8
  3 < 8 → take from left  → result=[1,3], i=1

Compare left[1]=5 vs right[1]=8
  5 < 8 → take from left  → result=[1,3,5], i=2

left exhausted → take rest of right → result=[1,3,5,8] ✅
 ```

 ```
 def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # divide
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])   # recurse left
    right = merge_sort(arr[mid:])   # recurse right

    # merge
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:     # ← <= keeps it STABLE
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]    # remaining left elements
    result += right[j:]   # remaining right elements
    return result
```

---

## Why O(n log n)?
```
DIVIDE:  splits in half each time
         [n] → [n/2][n/2] → [n/4]... → log n levels

MERGE:   at each level, merges ALL n elements
         level 1: merge n elements
         level 2: merge n elements
         level 3: merge n elements
         log n levels × O(n) each = O(n log n)

Visualized:
Level 0:  [5, 3, 8, 1]              n=4 comparisons
Level 1:  [5,3]    [8,1]            n=4 comparisons
Level 2:  [5][3]  [8][1]            n=4 comparisons
          ─────────────────────
          log(4)=2 levels × 4 = 8 total = O(n log n) ✅
```

---

## Complexity
```
Time:
  Best:    O(n log n)  ← always divides evenly
  Average: O(n log n)
  Worst:   O(n log n)  ← CONSISTENT — no bad cases!

Space:   O(n)   ← needs extra array for merging
Stable:  YES    ← equal elements keep original order
```

---

## Why Merge Sort Matters at Datadog
```
1. CONSISTENT O(n log n) — no worst case like quicksort
2. Used for COUNT INVERSIONS — confirmed Datadog question
3. Base of Timsort — Python's built-in sort
4. Great for EXTERNAL sorting (data too big for memory)
   → merge sorted chunks from disk
   → exactly what log processing does!
```

---

## Count Inversions — The Datadog Connection
```
Inversion = pair where left element > right element
[5, 3, 8, 1] has inversions: (5,3), (5,1), (3,1), (8,1) = 4 inversions

Brute force: O(n²) — check every pair
Merge sort:  O(n log n) — count during merge step

During merge, when right[j] < left[i]:
  ALL remaining left elements form inversions with right[j]
  inversions += len(left) - i
 ```



 
 # 2 — Quick Sort
 ```
 The Idea

Pick a PIVOT element.
Partition array:
  everything < pivot → LEFT side
  everything > pivot → RIGHT side
Recursively sort left and right.

Key insight: pivot ends up in its EXACT final position
             after partitioning. Forever. Never moves again.


Pick pivot = last element = 4

Partition:
[5, 3, 8, 1, 4]
              ↑ pivot = 4

Walk through:
  5 > 4 → goes right side
  3 < 4 → goes left side
  8 > 4 → goes right side
  1 < 4 → goes left side

Result:
  left=[3,1]  pivot=[4]  right=[5,8]
              ↑
         4 is now in FINAL position ✅

Recurse on left [3,1]:
  pivot=1 → left=[]  [1]  right=[3]
  → [1, 3]

Recurse on right [5,8]:
  pivot=8 → left=[5]  [8]  right=[]
  → [5, 8]

Final: [1,3] + [4] + [5,8] = [1,3,4,5,8] ✅
 ```

 ```
 def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]          # pick last element as pivot

    left  = [x for x in arr[:-1] if x <= pivot]  # < pivot
    right = [x for x in arr[:-1] if x > pivot]   # > pivot

    return quick_sort(left) + [pivot] + quick_sort(right)


## Why O(n log n) Average?
```
Good pivot (middle value):
  splits array roughly in half each time
  → log n levels × O(n) partition = O(n log n)

         [5,3,8,1,4]          level 0: n=5
            /     \
        [3,1]    [5,8]        level 1: n=5 total
        /   \    /   \
      [1]  [3][5]  [8]        level 2: n=5 total

log(5) levels × O(n) = O(n log n) ✅
```

---

## The Worst Case — O(n²)
```
Bad pivot = always smallest or largest element
          = already sorted array!

[1, 2, 3, 4, 5]  pivot=5
left=[1,2,3,4]   right=[]   ← completely unbalanced!

[1, 2, 3, 4]     pivot=4
left=[1,2,3]     right=[]   ← still unbalanced!

n levels × O(n) partition = O(n²) ❌

Fix: pick RANDOM pivot or MEDIAN of three
     arr[low], arr[mid], arr[high] → pick middle value
```
## Complexity
Time:
  Best:    O(n log n)  ← balanced splits
  Average: O(n log n)  ← random data
  Worst:   O(n²)       ← sorted/reverse sorted input

Space:   O(log n)  ← call stack depth
Stable:  NO        ← swapping changes relative order


                Merge Sort       Quick Sort
────────────────────────────────────────────────
Time worst      O(n log n)  ✅   O(n²)       ⚠️
Time average    O(n log n)       O(n log n)
Space           O(n)        ⚠️   O(log n)    ✅
Stable          YES         ✅   NO          ⚠️
Cache friendly  NO               YES         ✅
Used in Python  partially        NO
When to use     stability +      general purpose,
                guaranteed       memory constrained
                performance
```




 
 # 2 — Heap Sort
 ```
 ```

 ```
 ```



 
 # 2 — Counting Sort
 ```
 Instead of COMPARING elements, COUNT occurrences.
Then rebuild array from counts.

Only works for:
  ✅ integers
  ✅ known range [0, k]
  ✅ small range k

Step 1: count occurrences
  value:  1  2  3  4
  count: [1, 2, 1, 1]
          ↑
          1 appears once
             ↑
             2 appears twice

Step 2: rebuild array from counts
  1 appears 1 time → [1]
  2 appears 2 times → [1, 2, 2]
  3 appears 1 time → [1, 2, 2, 3]
  4 appears 1 time → [1, 2, 2, 3, 4] ✅
 ```

 ```
 pythondef counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count   = [0] * (max_val + 1)   # count array of size k

    # count occurrences
    for num in arr:
        count[num] += 1

    # rebuild sorted array
    result = []
    for val, freq in enumerate(count):
        result.extend([val] * freq)  # add val freq times

    return result
```

---

## Complexity
```
Time:   O(n + k)
          ↑   ↑
        count  rebuild
        array  sorted array
        n items  k buckets

Space:  O(k)   ← count array of size k

When k << n:   O(n) effectively ← FASTER than O(n log n)!
When k >> n:   O(k) wasteful ← worse than comparison sorts
```

---

## When to Use at Datadog
```
✅ Latency values in known range (0–1000ms)
✅ Error codes (known set of integers)
✅ Severity scores (1–5)
✅ HTTP status codes (100–599)

❌ Strings
❌ Floats
❌ Unknown range
❌ Very large range (k = 1,000,000)
```

---

## The One Thing to Remember
```
Counting sort = count occurrences, rebuild from counts
                O(n+k) time, O(k) space
                integers only, known range
                FASTER than O(n log n) when k is small
 ```




 
 # 2 — Timsort Sort
 ```
 Timsort = Merge Sort + Insertion Sort combined
          Invented for Python, now used in Java too

Key insight:
  Real world data is PARTIALLY sorted
  Timsort exploits this — finds already-sorted runs
  then merges them efficiently

Step 1: scan array for natural "runs"
        (already sorted sequences)

[3, 5, 7, 2, 4, 8, 1, 6]
 ↑─────↑  ↑─────↑  ↑──↑
 run 1     run 2    run 3

Step 2: if run too small → extend using insertion sort
        (insertion sort is fast on nearly sorted data)

Step 3: merge runs using merge sort
        [3,5,7] + [2,4,8] + [1,6]
        → [2,3,4,5,7,8] + [1,6]
        → [1,2,3,4,5,6,7,8] ✅


Time:
  Best:    O(n)        ← already sorted, one run
  Average: O(n log n)
  Worst:   O(n log n)

Space:   O(n)
Stable:  YES ✅

✅ Python's sorted() and list.sort() use Timsort
✅ Always stable
✅ Best case O(n) on nearly sorted data
✅ This is WHY Python sort is fast in practice

You never implement Timsort in interview.
Just say: "Python uses Timsort — O(n log n), stable"
 ```

 ```

 Algorithm      Best        Avg         Worst      Space   Stable
──────────────────────────────────────────────────────────────────
Bubble         O(n)        O(n²)       O(n²)      O(1)    YES
Selection      O(n²)       O(n²)       O(n²)      O(1)    NO
Insertion      O(n)        O(n²)       O(n²)      O(1)    YES
Merge          O(n log n)  O(n log n)  O(n log n) O(n)    YES
Quick          O(n log n)  O(n log n)  O(n²)      O(log n)NO
Heap           O(n log n)  O(n log n)  O(n log n) O(1)    NO
Counting       O(n+k)      O(n+k)      O(n+k)     O(k)    YES
Timsort        O(n)        O(n log n)  O(n log n) O(n)    YES


 "Which sort would you use?"

Strings/objects, stability needed → Timsort (Python default)
Guaranteed performance needed     → Merge Sort
Memory constrained                → Heap Sort (O(1) space)
General purpose, fastest avg      → Quick Sort (random pivot)
Small integers, known range       → Counting Sort
Nearly sorted data                → Insertion Sort
 ```



 
