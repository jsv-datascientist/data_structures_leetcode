import bisect

class LogStore:
    def __init__(self):
        self.logs = []   # sorted list of (timestamp, message)

    def insert(self, timestamp, message):
        bisect.insort(self.logs, (timestamp, message))
        # insort maintains sorted order automatically

    def query(self, start, end):
        # find left boundary — first log >= start
        left  = bisect.bisect_left(self.logs,  (start, ""))
        # find right boundary — first log > end
        right = bisect.bisect_right(self.logs, (end, "~"))

        return self.logs[left:right]
```

---

## Part B — Add Log Level Filter
```
Follow-up: "now filter by log level too"
  e.g. only return ERROR logs in time range