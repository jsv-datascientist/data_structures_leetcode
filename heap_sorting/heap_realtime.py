import heapq




def top_k_slowest_endpoints(endpoints, k):
    
    if not endpoints or k <= 0:
        return   []
    
    heap = []
    
    for endpoint, time in endpoints:
        heapq.heappush(heap, (time, endpoint))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [ (endpoint,time) for time, endpoint in sorted(heap, reverse= True)]


# max heap
def lowest_severity_score(logs, k):
    if not logs or k <= 0:
        return []
    
    heap = []
    for log in logs:
        heapq.heappush(heap,-log)
        if len(heap) > k:
            - heapq.heappop(heap)
    
    return [ -i for i in sorted(heap)]
        
    

def k_closest(servers, k):
    if not servers or k <= 0:
        return []

    heap = []
    for x, y in servers:
        dist = x**2 + y**2
        heapq.heappush(heap, (-dist, (x, y)))   # negate for max-heap
        if len(heap) > k:
            heapq.heappop(heap)                  # evict farthest

    return [(x, y) for _, (x, y) in sorted(heap, key=lambda x: x[0])]






if __name__ == "__main__":
    endpoints = [
    ("api/login",   120),
    ("api/metrics", 340),
    ("api/health",   45),
    ("api/traces",  210),
    ("api/logs",    890),
    ("api/alerts",  150),
    ("api/dash",    670),
]

top_3_slowest_endpoint = top_k_slowest_endpoints(endpoints, k=3)
print(top_3_slowest_endpoint)


logs = [45, 12, 67, 3, 89, 23, 56, 7, 34, 91]
result = lowest_severity_score(logs,k=5)
print(result)
