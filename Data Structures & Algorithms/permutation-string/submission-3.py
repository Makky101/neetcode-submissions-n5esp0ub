class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        for c in s1:
            s1Count[ord(c) - ord('a')] += 1
        
        wordCount = [0] * 26
        for i in range(len(s2)):
            wordCount[ord(s2[i]) - ord('a')] += 1

            if i >= len(s1):
                wordCount[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if wordCount == s1Count:
                return True
        return False