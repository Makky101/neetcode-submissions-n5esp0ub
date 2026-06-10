class Solution:
    def longestPalindrome(self, s: str) -> str:
        word = ''
        wordlen = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ((r - l) + 1) > wordlen:
                    word = s[l:r+1]
                    wordlen = len(word)
                
                l -= 1
                r += 1
            
            l,r = i , i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ((r - l) + 1) > wordlen:
                    word = s[l:r+1]
                    wordlen = len(word)
                
                l -= 1
                r += 1
        return word
