
## Remember
```
"top K"          → min-heap of size k

"k smallest"     → max-heap of size k

"merge streams"  → min-heap with (value, stream_index)

"median stream"  → two heaps

"k closest"      → max-heap of size k

Pattern name  = WHAT you're solving   → "top K"
Implementation = HOW you solve it     → min-heap of size k

Want K LARGEST  →  MIN-heap  (pop smallest, keep largest)
Want K SMALLEST →  MAX-heap  (pop largest, keep smallest)


"Python's built-in sorted() uses Timsort — O(n log n), stable, and optimal for most cases. For top-K problems I'd prefer a heap at O(n log k) since it's faster when k << n and works on streams. I'd only reach for a custom sort when I need a specific ordering key or need the full ranked output."


## Sorting Algorithms — What to Know

Datadog focuses on windowing techniques, sorting and searching, and practical tradeoffs under production constraints.  So know these by complexity, not implementation:

Algorithm       Time          Space    Stable   Know how?
────────────────────────────────────────────────────────
Timsort         O(n log n)    O(n)     YES      Python default — just use it
Merge Sort      O(n log n)    O(n)     YES      Know concept + inversion count
Quick Sort      O(n log n)*   O(log n) NO       Know concept + worst case O(n²)
Heap Sort       O(n log n)    O(1)     NO       Know via heapq
Counting Sort   O(n+k)        O(k)     YES      Know for integer ranges
```
## 1
```
You are a SRE. You have a list of API endpoints 
and their response times in milliseconds:

endpoints = [
    ("api/login",   120),
    ("api/metrics", 340),
    ("api/health",   45),
    ("api/traces",  210),
    ("api/logs",    890),
    ("api/alerts",  150),
    ("api/dash",    670),
]

Find the 3 SLOWEST endpoints (highest response time).

I give you a problem statement.
You tell me:
  1. Which pattern is this? -  Top k
  2. Min-heap or max-heap?  - Min - heap 
  3. What goes IN the heap? (what is the tuple?)    (reponse time, api emdpoints)
  4. Heap size limit?          heap size is 3
```

## Problem 2 🎯
```
You are monitoring 1 million server log lines.
Each log has a severity score (integer).

logs = [45, 12, 67, 3, 89, 23, 56, 7, 34, 91, ...]
                                    # 1 million entries

Find the 5 logs with the LOWEST severity scores.
(You cannot load all logs into memory at once)

  1. Which pattern is this? -  k lowest(smallest)
  2. Min-heap or max-heap?  - Max - heap 
  3. What goes IN the heap?   (serverity score)
  4. Heap size limit?          heap size is 5
  ```



  ## Problem 3 🎯
```
Datadog ingests logs from 3 different services.
Each service produces logs in chronological order.

service_a = [(1, "login"),    (4, "logout"),  (7, "error")]
service_b = [(2, "metric"),   (5, "alert"),   (8, "trace")]
service_c = [(3, "health"),   (6, "request"), (9, "timeout")]

             ↑ timestamp

Merge all 3 streams into one single chronological stream.

  1. Which pattern is this? -  Merge Stream
  2. Min-heap or max-heap?  - Min - heap 
  3. What goes IN the heap?   (value, list index, element indes)
  4. Heap size limit?         3
```

  ## Problem 4 🎯
```
A Datadog alerting system receives a continuous stream 
of metric values one at a time:

stream = [5, 15, 1, 3, 8, 7, 9, 2, 6, 12]

After each new value arrives, return the MEDIAN
of all values seen so far.

After 5        → median = 5
After 5,15     → median = 10.0
After 5,15,1   → median = 5
After 5,15,1,3 → median = 4.0

If you had ALL numbers upfront:
  [1, 3, 5, 8, 15] → sort → middle = 5  ✅ easy

But stream arrives ONE AT A TIME:
  You can't sort after every new number — too slow O(n log n) each time
  You need a smarter structure
===============================================================
Median = the MIDDLE value when all numbers are sorted.

What if we split all numbers into two halves?

Left half:  all numbers BELOW median  → [1, 3, 5]
Right half: all numbers ABOVE median  → [8, 15]

Median = max of left half   (if odd total)
       = avg of (max left, min right)  (if even total)
================================================================
Left half  → you need MAX quickly  → MAX-heap
Right half → you need MIN quickly  → MIN-heap

         MAX-heap          MIN-heap
         (left)            (right)
         
    3  ← root=5         8 ← root=8
   / \                  \
  1   2                  15

max of left = 5  (root of max-heap)  ← O(1)
min of right = 8 (root of min-heap)  ← O(1)

median = (5 + 8) / 2 = 6.5

================================================================
Step 1: Where does new number go?
        if new_num <= max of left → push to max_heap (negated)
        else                      → push to min_heap

Step 2: Rebalance if needed
        if max_heap has 2+ more than min_heap:
            move max_heap root → min_heap
        if min_heap is larger than max_heap:
            move min_heap root → max_heap

Step 3: Get median
        if len(max_heap) > len(min_heap):
            median = -max_heap[0]        ← root of max_heap
        else:
            median = (-max_heap[0] + min_heap[0]) / 2


================================================================
  1. Which pattern is this? -  Median
  2. Min-heap or max-heap?  - Min and Max heap 
  3. What goes IN the heap?   (value)
  4. Heap size limit?  varies with input
```

Problem 5 — Last One 🎯

```
Datadog tracks server locations on a 2D grid.
You are at the origin (0, 0).

servers = [
    (1,  3),   
    (4,  1),   
    (2,  2),   
    (5,  0),   
    (1,  1),   
    (3,  4),   
]

Find the 3 CLOSEST servers to the origin.

Distance formula = x² + y²  (no need for square root)

=========================================
You need to:
  → sort by DISTANCE        → distance goes in heap (sort key)
  → remember WHICH server   → server coordinates go in heap

So tuple = (?, ?)


# For max-heap, negate the sort key
heapq.heappush(heap, (-distance, server))
```

What is the distance formula for server (x, y)?
```
distance = x² + y²

server (1,1) → distance = 1² + 1² = 2
server (4,1) → distance = 4² + 1² = 17
server (2,2) → distance = 2² + 2² = 8
===================================================

  1. Which pattern is this? -  Closest
  2. Min-heap or max-heap?  - Max heap
  3. What goes IN the heap?   (value)
  4. Heap size limit? 3

```

