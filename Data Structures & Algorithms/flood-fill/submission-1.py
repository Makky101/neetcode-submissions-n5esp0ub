class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        oColour = image[sr][sc]

        def dfs(r,c):
            if r < 0 or r >= len(image):
                return
            if c < 0 or c >= len(image[0]):
                return
            
            if image[r][c] != oColour:
                return
            image[r][c] = color

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

            
            
        dfs(sr,sc)
        return image