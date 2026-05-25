class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        R,C = len(grid), len(grid[0])
        islands = []
        visit = set()

        def bfs(r,c,count):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))
            count = 1
            dirs = [(1,0),(0,-1),(0,1),(-1,0)]
            while queue:
                br,bc = queue.popleft()
                for dr,dc in dirs:
                    nr,nc = br + dr, bc + dc 
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] and (nr,nc) not in visit:
                            count += 1
                            queue.append((nr,nc))
                            visit.add((nr,nc))

            return count

        for rows in range(R):
            for cols in range(C):
                if grid[rows][cols] == 1 and (rows,cols) not in visit:
                    island = bfs(rows,cols,0)
                    islands.append(island)

        
        if islands:
            return max(islands)
        
        return 0
