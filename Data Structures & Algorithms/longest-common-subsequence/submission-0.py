class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for c in range(len(text2)-1,-1,-1):
            for r in range(len(text1)-1,-1,-1):
                if text2[c] == text1[r]:
                    matrix[r][c] = 1 + matrix[r+1][c+1]
                else:
                    matrix[r][c] = max(matrix[r][c+1],matrix[r+1][c])
        
        return matrix[0][0]