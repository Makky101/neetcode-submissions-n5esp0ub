class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_no = float('-inf')
        for i in range(len(nums)):
            num = nums[i]
            max_no = max(max_no,num)
            for j in range(i+1,len(nums)):
                num *= nums[j]  
                max_no = max(max_no,num)
        
        return max_no