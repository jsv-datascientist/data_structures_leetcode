"""

creating a keyword index. In this situation,
we are given a list of strings, with each string representing a document. 
Our task is to generate an index of all the distinct words in the documents for quick reference.
We need to create a dictionary where each unique word is a key, and the corresponding value is a list of
indices pointing to the documents where the word can be found.

Let's work through the solution. We first initialize an empty dictionary index. 
Then, we start looping through our list of documents. For each document we split
each document into words, and for each word, we check if it is already in our dictionary index. 
If it's in the dictionary, we append the current document's index to the list of indices for that word. 
If the word is not in the dictionary, then it's the first time we've seen this word,
and we add it to the index with a list that contains the current document's index as the value
"""

def keyword_index(docs):
    index = {}
    for doc_idx, doc in enumerate(docs):
        for word in doc.split():
            if word in index:
                index[word].append(doc_idx)
            else:
                index[word] = [doc_idx]
    return index
"""
**Visually:**
result = {
    "world": {        ← result["world"]
        0: 1          ← result["world"][0]
    }
}
"""
def keyword_index(docs):
    # implement this
    from collections import defaultdict
    result = defaultdict(defaultdict)
    for idx, doc in enumerate(docs):
        for word in doc.split():
            if word not in result:
                 result[word] = {}
            result[word][idx] = result[word].get(idx, 0) + 1 
            
    return result

docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}