"""
Let's get started. You're given a stream of strings. Each string is either a 
Query starting with Q: or a Log line starting with L:. For every log line, output which 
queries match it — a query matches a log if every word in the query appears in the log.

stream = [
  "Q: database",
  "Q: loading failed",
  "L: Database service started",
  "Q: fail",
  "L: Loading main DB snapshot",
  "L: Loading snapshot failed no stacktrace",
]

Output:
L: Database service started       → ["database"]
L: Loading main DB snapshot       → ["database"]
L: Loading snapshot failed ...    → ["database", "loading failed", "fail"]


stream = [
  "Q: database",
  "Q: loading failed",
  "L: Database service started",
  "Q: fail",
  "L: Loading main DB snapshot",
  "L: Loading snapshot failed no stacktrace",
]
```

**Step 1:** `Q: database`
```
queries = [
  ("database",  {"database"})
]
```

**Step 2:** `Q: loading failed`
```
queries = [
  ("database",       {"database"}),
  ("loading failed", {"loading", "failed"})
]
```

**Step 3:** `L: Database service started`
```
log_words = {"database", "service", "started"}   ← lowercased

Check "database"      → {"database"} ⊆ {"database","service","started"} ✅
Check "loading failed"→ {"loading","failed"} ⊆ {"database","service","started"} ❌

result = {
  "L: Database service started": ["database"]
}
```

**Step 4:** `Q: fail`
```
queries = [
  ("database",       {"database"}),
  ("loading failed", {"loading", "failed"}),
  ("fail",           {"fail"})
]
```

**Step 5:** `L: Loading main DB snapshot`
```
log_words = {"loading", "main", "db", "snapshot"}

Check "database"       → {"database"} ⊆ log_words? ❌
Check "loading failed" → {"loading","failed"} ⊆ log_words? ❌ (no "failed")
Check "fail"           → {"fail"} ⊆ log_words? ❌

result = {
  "L: Database service started": ["database"],
  "L: Loading main DB snapshot":  []           ← no matches
}
```

**Step 6:** `L: Loading snapshot failed no stacktrace`
```
log_words = {"loading","snapshot","failed","no","stacktrace"}

Check "database"       → {"database"} ⊆ log_words? ❌
Check "loading failed" → {"loading","failed"} ⊆ log_words? ✅
Check "fail"           → {"fail"} ⊆ log_words? ❌ ("fail" ≠ "failed")

result = {
  "L: Database service started":          ["database"],
  "L: Loading snapshot failed ...":       ["loading failed"]
}


"""

def livetail(stream):
    
    if not stream: 
        return {}
    
    
    result = {}
    queries = []  # list of set ( original word, word_set)
    
    for line in stream: 
        line_lower = line.lower()
        
        if line_lower.startswith("q:"): 
          original_query = line[3:].strip()  # Database , Loading failed
          query_word_set = set(line_lower[3:].split()) # {database}, {loading, failed}
          queries.append((original_query, query_word_set))
          print(queries)
            
        elif line_lower.startswith("l:"):
          original_log = line[3:].strip()
          log_word_set = set(line_lower[3:].split())
          
          match=[]
          
          for original_query, query_word_set in queries : 
            if query_word_set.issubset(log_word_set):
              match.append(original_query)
            
          result[original_log] = match
            
    return result
  
  
if __name__ == "__main__" :
    
    stream = [
      "Q: database",
      "Q: loading failed",
      "L: Database service started",
      "Q: fail",
      "L: Loading main DB snapshot",
      "L: Loading snapshot failed no stacktrace",
    ]
    
    #print( livetail(["Q: database", "Q: error"] )  # → {})
          
    result = livetail(stream)
    
    print(result)       
          
            