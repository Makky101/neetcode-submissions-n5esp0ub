class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first == second:
                continue
            else:
                first = first - second
                heapq.heappush(max_heap,-first)

        if max_heap:
            return -heapq.heappop(max_heap)
        else:
            return 0
            
