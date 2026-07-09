class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        checker = 0
        for _ in range(len(nums)):
            if checker in nums:
                checker += 1
            else:
                break
        return checker