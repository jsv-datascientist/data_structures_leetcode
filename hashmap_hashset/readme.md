
```
seen, repeated = set(), set()
for num in nums:
    if num in seen:
        repeated.add(num)
    else: 
        seen.add(num)

return list(seen-repeated)
# product that are seen but not repeated



You have two lists named inventory1 and inventory2 representing the clothing items from these stores. Now, your prime mission is to figure out the clothes that are exclusive to each store. Note that the letter casing is not important, so items like "t-shirt" and "T-Shirt" are considered the same. Return all exclusive clothes sorted in alphabetical order.

Keep in mind that we're dealing with text data here. The length of these lists can range from as few as no items to as many as a star cluster. There is zero room for error, kid. Now, get to it!

Hint: To compare items, ignoring the casing, convert all elements to uppercase.

names_list = ['name1', 'name2', 'name3']

upper_list = [name.upper() for name in names_list]

# ['NAME1', 'NAME2', 'NAME3']


names_set = {'name1', 'name2', 'name3'}

upper_set = {name.upper() for name in names_set}

# {'NAME1', 'NAME2', 'NAME3'}
```

```
 Imagine you're working on a text analyzing tool that needs to identify the first unique word in a piece of text.

def find_unique_string(words):
    seen = set()
    duplicates = set()
    
    for word in words:
        if word in seen:
            duplicates.add(word)
        seen.add(word)
        
    for word in words:
        if word not in duplicates:
        return word

return ""


 ```

 ```
 ```


 ```
 ```


 ```
 ```