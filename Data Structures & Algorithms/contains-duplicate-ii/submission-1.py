class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False
        hashSet = {}
        for i in range(len(nums)):
            if nums[i] in hashSet:
                j = hashSet[nums[i]]
                op = abs(i - j)
                if op <= k:
                    return True
                elif op > k:
                    hashSet.clear()
                    hashSet[nums[i]] = i
            else:
                hashSet[nums[i]] = i

        return False