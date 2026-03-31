class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 1:
            return False
        seen = []
        while n != 1:
            tot = 0
            while n > 0:
                digit = n % 10
                print('digit -->',digit)
                tot += digit ** 2
                print('tot -->',tot)
                n //= 10
                print('n -->',n)
            if tot in seen:
                return False
            n = tot
            print('the new n -->',n)
            seen.append(tot)
        return True