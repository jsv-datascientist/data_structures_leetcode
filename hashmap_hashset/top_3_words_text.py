"""
magine being asked to construct a simple word frequency analyzer. 
Given a large body of text, we need to identify the three most frequently occurring words.
Imagine working with large documents, such as news articles, thesis manuscripts, or even books. 
Identifying the most common words could give us an overview of the main themes or topics in the text.


An initial thought might be to iterate over the entire set of words, 
count each word's occurrences, and then compare the counts.
However, this method would involve repetitive and redundant operations and is, therefore, inefficient. 
If we think back to the theory of computational complexity from our earlier lessons, t
his 'brute force' approach is known to have a time complexity of 
O(N2),
N is the total number of words. That's not very appealing, right? Hence, we need to find an alternative approach that's more time-efficient.
"""