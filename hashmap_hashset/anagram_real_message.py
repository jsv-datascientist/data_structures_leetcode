from collections import defaultdict


"""
ou'll be given two arrays of words. Your task? 
Find the unique words in the first array that can rearrange their 
letters to match at least one word in the second array. Like transforming 'cinema' into 'iceman'

O((n+m)⋅wlogw+P)
Consider a cryptology scenario. You've intercepted two separate messages, 
each consisting of a list of coded words. You suspect that there might be some 
connection between the two messages - specifically, that some words from 
one list are anagrams of words in the other list. Your goal is to find these
pairs of anagram words to decipher the code.
"""
def anagram(list_1, list_2):
    # Create mapping for `list_1`
    mapping_1 = defaultdict(list)
    # mapping_1 stores (sorted anagram) -> list[anagrams] mapping for `list_1`
    for word in list_1:
        sorted_tuple = tuple(sorted(word)) # unique identifier of the anagram
        mapping_1[sorted_tuple].append(word)
        # `mapping_1[sorted_tuple]` stores all anagrams under the same identifier for `list_1`

    # Create mapping for `list_2`
    mapping_2 = defaultdict(list)
    # mapping_2 stores (sorted anagram) -> list[anagrams] mapping for `list_2`
    for word in list_2:
        sorted_tuple = tuple(sorted(word)) # unique identifier of the anagram
        mapping_2[sorted_tuple].append(word)
        # `mapping_2[sorted_tuple]` stores all anagrams under the same identifier for `list_2`

    # Intersect keys from mapping_1 and mapping_2 to get common sorted tuples
    # Every element in `common_tuples` is an anagram identifier that exists in both lists
    common_tuples = set(mapping_1.keys()) & set(mapping_2.keys())

    output = []
    for anagram_tuple in common_tuples:
        for word1 in mapping_1[anagram_tuple]:
            for word2 in mapping_2[anagram_tuple]:
                # Both word1 and word2 have the same anagram identifier, so are anagrams
                output.append((word1, word2))

    return output