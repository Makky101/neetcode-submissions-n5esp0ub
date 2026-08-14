class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]
        res = []
        while arr:
            max_i = 0
            for i in range(1,len(arr)):
                if arr[i] + arr[max_i] > arr[max_i] + arr[i]:
                    max_i = i
            res.append(arr[max_i])
            arr.pop(max_i)
        
        res = "".join(res)

        return res if res[0] != '0' else '0'
