class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        count = 0
        mul = x
        print('mul ->',mul)
        inverse = None
        if n < 0:
            inverse = n
            n = (n - n) - n
        while count < n-1:
            x *= mul
            print('x ->',x)
            count += 1
            print('count ->',count)
        
        if inverse:
            x = 1 / x
        return x