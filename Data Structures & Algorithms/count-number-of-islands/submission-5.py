class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m ,n = len(grid), len(grid[0])
        island = 0
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return 
            
            grid[r][c] = '0'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
                

        for rows in range(m):
            for cols in range(n):
                if grid[rows][cols] == '1':
                    dfs(rows,cols)
                    island += 1

        return island