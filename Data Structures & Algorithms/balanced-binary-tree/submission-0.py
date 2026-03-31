# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.hmm = True
        def dfs(node):
            res = 0
            if node is None:
                return 0
            right = dfs(node.right)
            left = dfs(node.left)
            diff = abs(left - right)
            res = max(left,right) + 1
            if diff > 1:
                self.hmm = False
            return res

        dfs(root)

        return self.hmm