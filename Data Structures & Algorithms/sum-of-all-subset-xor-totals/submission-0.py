class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        path = []
        total = []
        def dfs(start):
            if len(path) == 1:
                total.append(path[0])
            else:
                res = 0
                for num in path:
                    res ^= num
                total.append(res)
            
            for i in range(start,len(nums)):
                digit = nums[i]
                path.append(digit)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return sum(total)