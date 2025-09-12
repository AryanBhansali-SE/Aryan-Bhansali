''' Top K frequent Elements'''




from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
       
        heap = []
        for num, cnt in freq.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)        
       
        return [num for _, num in heap]


print(Solution().topKFrequent([1,1,1,2,2,3], 2))


print(Solution().topKFrequent([1], 1))


print(Solution().topKFrequent([4,4,4,6,6,7,7,7,7,8], 2))







