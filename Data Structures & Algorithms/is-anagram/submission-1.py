class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store1 = {}
        for char in s:
            if char in store1:
                store1[char] += 1
            else:
                store1[char] = 1

        store2 = {}
        for char in t:
            if char in store2:
                store2[char] += 1
            else:
                store2[char] = 1

        if store1 == store2:
            return True 
        else:
            return False
