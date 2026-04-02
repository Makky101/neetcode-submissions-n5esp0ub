class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [((x - 0)**2 + (y - 0)**2,x,y) for x,y in points]
        res = []
        heapq.heapify(min_heap)

        for _ in range(k):
            _,x,y = heapq.heappop(min_heap)
            res.append([x,y])
        
        return res