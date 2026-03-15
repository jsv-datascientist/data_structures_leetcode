"""
LRU = Least Recently Used

It's a cache eviction policy:
  Cache has a fixed capacity.
  When cache is full and new item arrives,
  evict the LEAST RECENTLY USED item.
  
Datadog caches metric queries in memory.
Cache size is limited — can't store everything.

When a new metric query comes in:
  → if already cached → return it (cache hit)
  → if not cached → fetch it, store it
  → if cache full → evict least recently used query
                    make room for new one
                    
 Most Recently Used               Least Recently Used
─────────────────────────────────────────────────────
[page4] → [page1] → [page3] → [page2]
  ↑                               ↑
  just accessed                   evict this if full

Every time you ACCESS an item → moves to FRONT
When cache FULL → remove from BACK          




get(key):
  → if key exists: return value, mark as recently used
  → if key missing: return -1

put(key, value):
  → if key exists: update value, mark as recently used
  → if key missing: insert
      → if over capacity: evict LRU first
      
      
from collections import OrderedDict
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od.move_to_end("a")       # moves "a" to back
od.move_to_end("b", last=False)  # moves "b" to front   

a, b, c 

(last)a → b → c  (first) 
last==false 
"""
from collections import OrderedDict 
class LURCache:
    
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        self.cache[key] = value
        
        if key in self.cache:
            self.cache.move_to_end(key)
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    