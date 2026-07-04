class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) / 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            new_dp=set() 
            for t in dp:
                new_dp.add(t)
                new_dp.add(t + nums[i])
            dp=new_dp
        
        return True if target in dp else False  