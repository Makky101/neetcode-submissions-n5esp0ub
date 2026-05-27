class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        m, n, = len(grid), len(grid[0])
        seen = 0
        count_good = 0
        count_bad = 0
        time = 0

        queue = deque()
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        for rows in range(m):
            for cols in range(n):
                if grid[rows][cols] == 1:
                    count_good += 1
                elif grid[rows][cols] == 2:
                    queue.append((rows,cols))
        
        while queue:
            infected = False
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in dirs:
                    nr,nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr,nc))
                            infected = True
                            seen += 1
            if infected:
                time += 1
        
        if seen != count_good:
            return -1
        
        return time
