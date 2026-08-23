class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        count =  0

        for c in s:
            if c == ']':
                count += 1
            else:
                count -= 1

            res = max(res,count)
        
        
        res = (res+1)//2
        
        return res


        