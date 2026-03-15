"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
 
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.



SOLUTION :
HashMap/Set — we need O(n) so no sorting. Use a set for O(1) lookups.

Set - No duplicate, un ordered, used hash map internally 

pythons = {1, 2, 3}
s[0]   # ❌ TypeError — sets have no index
```

---

## How It Works Under the Hood

A set uses a **hash table** internally.
```
value → hash function → bucket position

99  → hash(99)  → slot 42 → empty → False
1   → hash(1)   → slot 7  → found → True

# Creates a set — duplicates are auto-removed
s = {1, 2, 3, 3, 3}
print(s)  # {1, 2, 3}

# From a list
nums = [100, 4, 200, 1, 3, 2]
s = set(nums)
print(s)  # {1, 2, 3, 4, 100, 200

"""

class solution: 
    def longestet_consecutive_sequence(self, nums):
        
        """
        Only start counting from the beginning of a sequence.
        A number is a sequence start if n-1 does NOT exist in the set.
        nums = [100, 4, 200, 1, 3, 2]

        Is 100 a start? → 99 in set? No  ✅ start → count: 100, 101? No → length 1
        Is 4 a start?   → 3 in set?  Yes ❌ skip
        Is 200 a start? → 199 in set? No ✅ start → count: 200, 201? No → length 1
        Is 1 a start?   → 0 in set?  No  ✅ start → count: 1,2,3,4,5? No → length 4 ✅
        """
        
        # remove any duplicates
        num_set = set(nums)  #for o(1) lookup
        best = 0 
        
        for n in num_set: 
            if (n-1) not in num_set:
                length = 1
                
                while (n+length in num_set):
                    length += 1
                best = max(best, length)
        return best


if __name__ == "__main__" :
    
         nums = [100, 4, 200, 1, 3, 2]
         
         sol = solution()
         result = sol.longestet_consecutive_sequence(nums)
         
         print(result)