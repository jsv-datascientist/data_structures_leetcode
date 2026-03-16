import re
from collections import defaultdict

"""
print(rare_words_finder("Hey there hot shot Are you ready for a challenge This might be trickier than it looks")) 
# Expected Output: [('hey', 1), ('there', 1), ('hot', 1), ('shot', 1), ('are', 1)]

print(rare_words_finder("The quick brown fox jumps over the lazy dog The fox is quick but the dog is lazy")) 
# Expected Output: [('brown', 1), ('jumps', 1), ('over', 1), ('but', 1), ('quick', 2)]

print(rare_words_finder("")) # Expected Output: []
"""
def rare_words_finder(text):
    # implement this
    text = re.sub(r'[^a-z\s]',"",text.lower())
    print(text)
    words_list = text.split()
    word_count = defaultdict(int)
    
    for word in words_list:
        word_count[word] += 1
    
    return sorted(word_count.items(), key = lambda x: x[1])[:5]