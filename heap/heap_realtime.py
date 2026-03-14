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