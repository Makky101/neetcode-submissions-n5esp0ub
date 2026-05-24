class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m ,n = len(grid), len(grid[0])
        island  = seen = 0
        def dfs(r,c,isl):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return 0
            
            grid[r][c] = '0'
            isl += dfs(r-1,c,isl)
            isl += dfs(r+1,c,isl)
            isl += dfs(r,c+1,isl)
            isl += dfs(r,c-1,isl)
            isl += 1
            return isl
                

        for rows in range(m):
            for cols in range(n):
                if grid[rows][cols] == '1':
                    seen += dfs(rows,cols,seen)
                    if seen:
                        island += 1

        return island