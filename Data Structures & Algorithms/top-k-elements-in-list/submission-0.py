class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for i in range(k):
            count = -1
            key = None

            for keys in freq:
                value = freq[keys]
                if value > count:
                    count = value
                    key = keys

            result.append(key)        
            freq[key] = -1

        return result




            
