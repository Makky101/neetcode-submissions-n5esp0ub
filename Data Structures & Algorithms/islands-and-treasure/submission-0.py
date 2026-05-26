class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M,N = len(grid), len(grid[0])
        queue = deque()
        for rows in range(M):
            for cols in range(N):
                if grid[rows][cols] == 0:
                    queue.append((rows,cols))
        
        while queue:
            r,c = queue.popleft()
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < M and 0 <= nc < N:
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr,nc))