
## Remember

"top K"          → min-heap of size k

"k smallest"     → max-heap of size k

"merge streams"  → min-heap with (value, stream_index)

"median stream"  → two heaps

"k closest"      → max-heap of size k

Pattern name  = WHAT you're solving   → "top K"
Implementation = HOW you solve it     → min-heap of size k

## 1

You are a SRE. You have a list of API endpoints 
and their response times in milliseconds:

endpoints = [
    ("api/login",   120),
    ("api/metrics", 340),
    ("api/health",   45),
    ("api/traces",  210),
    ("api/logs",    890),
    ("api/alerts",  150),
    ("api/dash",    670),
]

Find the 3 SLOWEST endpoints (highest response time).

I give you a problem statement.
You tell me:
  1. Which pattern is this? -  Top k

  2. Min-heap or max-heap?  - Min - heap 

  3. What goes IN the heap? (what is the tuple?)    (reponse time, api emdpoints)

  4. Heap size limit?          heap size is 3

