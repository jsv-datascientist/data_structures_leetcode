"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.


Solution
==============
The Problem
groups[key] = s would overwrite — every new word with the same key replaces the previous one.
pythongroups[('a','e','t')] = "eat"   # ✅
groups[('a','e','t')] = "tea"   # ❌ "eat" is GONE now
groups[('a','e','t')] = "ate"   # ❌ "tea" is GONE now

What You Want
Multiple words can share the same key — you need a list to collect them all:
pythongroups[('a','e','t')].append("eat")  # ["eat"]
groups[('a','e','t')].append("tea")  # ["eat", "tea"]
groups[('a','e','t')].append("ate")  # ["eat", "tea", "ate"]

# result: {('a','e','t'): ["eat", "tea", "ate"]}  ✅

"""

from collections import defaultdict


class solution:
    
    def group_anagram(self,str):
        
        result = defaultdict(list)
        
        for s in str: 
            
            key = tuple(sorted(s))
            result[key].append(s)
        return list(result.values())

if __name__ == "__main__":
    
    str =  ["eat","tea","tan","ate","nat","bat"]
    
    sol = solution()
    result = sol.group_anagram(str)
    

    print(f"output is {result} ")
