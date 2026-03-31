class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        verify = "".join(sorted(s1))
        l = 0
        r = len(s1) - 1
        while r != len(s2):
            subString = s2[l : r + 1]
            checker = "".join(sorted(subString))
            if verify == checker:
                return True
            l += 1
            r += 1
        return False