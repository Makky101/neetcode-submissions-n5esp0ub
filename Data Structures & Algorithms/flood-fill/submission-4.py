class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        m , n = len(image), len(image[0])
        orig = image[sr][sc]
        queue = deque([(sr,sc)])
        image[sr][sc] = color
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        while queue:
            r,c = queue.popleft()

            for dr,dc in dirs:
                nr , nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == orig:
                    image[nr][nc] = color
                    queue.append((nr,nc))
        
        return image
