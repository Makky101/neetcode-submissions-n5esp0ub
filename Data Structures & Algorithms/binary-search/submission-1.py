class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                l += 1
            else:
                r -= 1
        return -1
        