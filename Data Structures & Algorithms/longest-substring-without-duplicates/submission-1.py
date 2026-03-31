class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        for i in range(len(s)):
            count = 1
            seen.add(s[i])
            l = i + 1
            while l < len(s) and s[l] not in seen:
                count += 1
                seen.add(s[l])
                l += 1
            longest = max(longest, count)
            seen.clear()
        return longest
