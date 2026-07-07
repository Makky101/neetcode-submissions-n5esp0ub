class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            c = 0
            for j in range(n):
                if (1 << j) & i:
                    c += 1
            l.append(c)

        return l