class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        checker = 0
        for num in nums:
            if checker in nums:
                checker += 1
            else:
                break
        return checker