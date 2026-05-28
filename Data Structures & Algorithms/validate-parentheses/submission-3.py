class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        isValid = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for string in s:
            if stack and string in isValid and stack[-1] == isValid[string]:
                stack.pop()
            else:
                stack.append(string)
        
        if len(stack) == 0:
            return True
        else:
            return False