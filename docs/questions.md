
# Topic 1 — Longest Consecutive Sequence
```
arr = [100, 4, 200, 1, 3, 2]

What is the longest consecutive sequence   
 [1,2,3,4]

what is its length? 
4

Why do we use a HashSet instead of sorting?
NIf we consider each number is start, we need to find the next elelent
for that hastset is better for look up with o(1) 

What is the time complexity of each approach?
Explain What is the condition that prevents O(n²)?
We have take one as start eleme,t and other next to it as the second element and loop inside loop we can check across each element, it would be o(n2), so to avoid it , we can  consider taking on element as start, if the n-1 exists , we skip else we check for the next7


The key condition:
  only START counting if num-1 NOT in set
  → guarantees we only start at sequence beginnings
  → inner while loop only runs for actual sequences
  → each element visited at most twice total
  → O(n) overall, not O(n²)


arr = [5, 3, 1, 2, 4]

Trace through the algorithm:
  1. What goes in the HashSet?
  {1, 2,3 ,4,5}

  2. Which numbers trigger the "start counting" condition?
  1

  3. What is the longest sequence length?
  5
```