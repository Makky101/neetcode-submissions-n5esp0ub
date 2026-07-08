class Solution:
    def reverseBits(self, n: int) -> int:
        value=0
        for i in range(32):
            res = (n >> i) & 1
            value |= res <<  (31-i)
        return value