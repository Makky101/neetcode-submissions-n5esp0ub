class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = [-n for n in nums]
        self.k = k
        heapq.heapify(self.arr)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.arr,-val)
        clone = self.arr.copy()
        for _ in range(self.k - 1):
            heapq.heappop(clone)

        return -heapq.heappop(clone)
