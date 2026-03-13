
"""
"Let's get started. You're given a list of positive integer latencies,
a number of buckets and a bucket width. Write a function that calculates
how frequently each range of latencies occurs.
The first bucket always starts at 0. For example:
latencies   = [3, 15, 7, 22, 31, 10, 5]
num_buckets = 4
bucket_width= 10

Buckets: 0-9, 10-19, 20-29, >=30
Output:  [3, 2, 1, 1]


# 1. edge cases — empty list, zero width
# 2. init counts array of size num_buckets with zeros
# 3. for each latency → compute index → clamp → increment
# 4. return counts

Time:  O(n)  — one pass through latencies
Space: O(k)  — counts array of size num_buckets

n = number of latencies
k = number of bucket

"""

def latency_histogram(latencies, num_buckets, bucket_width):
    
    if not latencies:
        return [0] * num_buckets 
    
    if bucket_width == 0:
        raise ValueError("Bucket width needs to be > than 0")
    
    count = [0] * num_buckets # [0 0 0 0]
    for latency in latencies: 
        
        idx = latency // bucket_width
        
        idx = min(idx, num_buckets  -1)
        count[idx] += 1
        # yeild count[:]  # this is done for infinite latency , not yeild count because the previous ones are overridden , so
        # count[:] make copy each time
    
    return count    #← only returns AFTER loop ends, how about for the infinite latency

if __name__ == "__main__" :
    latencies   = [3, 15, 7, 22, 31, 10, 5]
    num_buckets = 4
    bucket_width= 10
    
    result = latency_histogram(latencies, num_buckets, bucket_width)
    print(result)
    
        
        
    
    