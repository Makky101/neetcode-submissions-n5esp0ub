class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return
    
        num = []

        number = ''
        for digit in digits:
            number += str(digit)

        number = str(int(number) + 1)

        for digit in number:
            num.append(int(digit))

        return num