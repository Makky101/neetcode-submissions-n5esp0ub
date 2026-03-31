class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin = leftmax = 0

        for c in s:
            if c == '(':
                leftmin += 1
                leftmax += 1
            elif c == ')':
                leftmin -= 1
                leftmax -= 1
            else:
                leftmin -= 1
                leftmax += 1
            
            leftmin = max(leftmin, 0)

            if leftmax < 0:
                return False
        
        
        return leftmin == 0