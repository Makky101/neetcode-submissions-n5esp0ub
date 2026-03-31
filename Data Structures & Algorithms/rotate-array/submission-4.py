class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arrL = len(nums)
        hashMap = {}
        for i in range(arrL):
            pos = i + k
            if pos >= arrL:
                pos = pos % arrL
            hashMap[pos] = nums[i]
        
        for n in hashMap:
            nums[n] = hashMap[n]
        
        return nums