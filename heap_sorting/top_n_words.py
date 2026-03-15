import heapq
import re

"""
Given a string paragraph and an integer n, implement a function top_n_frequent_words 
that returns the top n most frequent words in the paragraph along with their frequencies.


## When to Use Heap — Pattern Recognition
```
"top K"          → min-heap of size k
"k smallest"     → max-heap of size k
"merge streams"  → min-heap with (value, stream_index)
"median stream"  → two heaps (max-heap + min-heap)
"k closest"      → max-heap of size k
```
"""
def top_n_frequent_words (para, k):
    
    if not para or k <= 0:
        return []
    
    #first put all in dict as (word, count)
    freq={}
    # r'[^a-z\s]' means:
    # ^ = NOT
    # a-z = letters
    # \s = whitespace
    # → remove everything that is NOT a letter or space
    # re.sub(r'[^a-b\s]','',para.lower())
    
    for word in para.lower().replace(".","").split():
        freq[word] = freq.get(word,0) + 1
    
    # then sort either by sort or heap 
    # if we do worting it would be O(n log n) sorted = sort(feeq.items(), key = lambda x : (-x[1], x[0]))
    
    heap = []
    
    for word,count in freq.items():
        heapq.heappush(heap,(count,word))
        if len(heap) > k:
            heapq.heappop(heap)
    #reverse=True means DESCENDING overall. (z-a) for tie cases
    return [ (word, count) for count, word in sorted(heap, reverse=True) ] 
    
    




if __name__ == "__main__":
    paragraph = """
    Herbal sauna uses the healing properties of herbs in combination 
    with distilled water. The water evaporates and distributes the 
    effect of the herbs throughout the room. A visit to the herbal 
    sauna can cause miracles especially for colds.
    """

    k = 3
    # Expected output:
    # [("the", 4), ("herbal", 2), ("herbs", 2)]
    result =top_n_frequent_words (paragraph, k)
    print(result)