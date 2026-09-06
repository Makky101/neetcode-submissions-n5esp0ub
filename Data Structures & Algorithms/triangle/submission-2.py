class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = {}
        def takeMin(layer,idx):
            if layer == len(triangle)-1:
                return triangle[layer][idx] 
            if (layer,idx) in cache:
                return cache[(layer,idx)]
            cache[(layer,idx)] = triangle[layer][idx]  + min(takeMin(layer+1,idx),takeMin(layer+1,idx+1))
            return cache[(layer,idx)]

        return takeMin(0,0)