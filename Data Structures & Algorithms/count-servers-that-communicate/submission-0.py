class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])

        row_cnt = [0] * r
        col_cnt = [0] * c

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    row_cnt[row] += 1
                    col_cnt[col] += 1
        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and max(row_cnt[row],col_cnt[col]) > 1:
                    res += 1
        
        return res