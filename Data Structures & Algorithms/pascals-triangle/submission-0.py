class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        pp = [1]

        if numRows == 1:
            return res

        for i in range(1,numRows):
            pack = []
            for j in range(i):
                if j == 0:
                    pack.append(pp[0])
                
                if j < len(pp) - 1:
                    total = pp[j] + pp[j+1]
                    pack.append(total)
                else:
                    pack.append(pp[j])
            res.append(pack)
            pp = pack
        
        return res