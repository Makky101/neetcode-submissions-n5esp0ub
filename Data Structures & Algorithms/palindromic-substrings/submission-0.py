class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for l in range(len(s)):
            for r in range(l,len(s)):
                word = s[l:r+1]
                if word == word[::-1]:
                    count += 1 

        return count     
