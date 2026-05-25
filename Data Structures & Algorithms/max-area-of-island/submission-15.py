class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        R,C = len(grid), len(grid[0])
        max_area = 0

        def dfs(r,c):
            if r < 0 or r >= R or c < 0 or c >= C or not grid[r][c]:
                return 0
            
            grid[r][c] = 0
            right = dfs(r+1,c)
            left = dfs(r-1,c)
            up = dfs(r,c+1)
            down = dfs(r,c-1)

            return 1 + left + right + up + down

        for rows in range(R):
            for cols in range(C):
                if grid[rows][cols] == 1:
                    max_area = max(max_area,dfs(rows,cols))
        
        return max_area