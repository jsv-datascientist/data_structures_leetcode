



    """
    lists = [
        [1, 4, 7],     ← list 0  (3 elements)
        [2, 5, 8],     ← list 1  (3 elements)
        [3, 6, 9],     ← list 2  (3 elements)
        ]
    K is the num of list 
    n is the no of elements in each list 
    
    no of cuts = log n 
    8 -> 4 -> 2 - 1 = 3 cuts, log 8, 3
    16 = 4 
    1024 = log 1024 = 10
    
    k=3 lists → heap has 3 elements → tree height = log₂3 ≈ 1.6
    k = 3, height of tree = log 3 = 1.6 
    k=8 lists → heap has 8 elements → tree height = log₂8 = 3
    k=1000 lists → heap has 1000 elements → tree height = log₂1000 ≈ 10
    
    Say n = 1,000,000 total elements across k = 100 lists

    O(n log n) = 1,000,000 × log(1,000,000) = 1,000,000 × 20 = 20,000,000 ops
    O(n log k) = 1,000,000 × log(100)       = 1,000,000 ×  7 =  7,000,000 ops
    
    DD _ a few hundred metric streams (small k) with millions of data points (huge n).
    =============================
    You're at Datadog's ops center. 3 engineers are each reading out server metric values from their sorted log stream, one at a time. Your job is to write them down in order.
    You look at what each engineer is currently holding up:

    Engineer 0 holds → 1
    Engineer 1 holds → 2
    Engineer 2 holds → 3

    You take the smallest (1 from Engineer 0), write it down. Now Engineer 0 shows you their next card: 4.
    Repeat forever.
    =========================
    SEED  →  POP  →  REPLACE
    SEED — fill heap with the first element of every list once.
    POP — extract the minimum (it's always at the top).
    REPLACE — push the next element from the same list the popped element came from.
    ====================================================
    The heap stores tuples. Remember **VLI**:
    ```
    V = Value       (so heap knows what to compare)
    L = List index  (so we know which list to pull next from)
    I = Element index (so we know where we are in that list)
    =======================================================
    
    You're given k sorted arrays of integers. 
    Write a function that merges them all into a single sorted array and returns it.
    Input:  [[1,4,7], [2,5,8], [3,6,9]]
    Output: [1,2,3,4,5,6,7,8,9]
    """
    import heapq
    def merge_list(lists):
        
        if not lists : 
            return []
        
        heap = []
        result = []
        
        for i, lst in enumerate(lists):
            if lst :
                heapq.heappush( heap, (lst[0], i, 0) )  # VLI
                
        while heap: 
            value, lst_idx, element_idx = heapq.heappop(heap)
            
            result.append(value)
            
            next_idx = element_idx + 1
            
            if next_idx < len(lists[lst_idx]):
                heapq.heappush(heap, (lists[lst_idx][next_idx], lst_idx, next_idx))
                
        
        return result


if __name__ == "__main__" :
    
    lists = [[1,4,7], [2,5,8], [3,6,9]]
    
    result = merge_list(lists)
    
    print(result)
    
    
    