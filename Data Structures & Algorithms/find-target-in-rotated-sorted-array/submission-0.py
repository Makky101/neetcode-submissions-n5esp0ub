class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid

            #left sorted portion
            if nums[l] <= nums[mid]:
                #it would not be there
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                #it could be there
                else:
                    r = mid - 1

            #right sorted portion
            else:
                #it would not be there
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                #it could be there
                else:
                    l = mid + 1
        
        return -1