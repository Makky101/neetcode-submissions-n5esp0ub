# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode],res=[]) -> List[int]:
        res = []
        def result(root):
            if root is None:
                return 
            result(root.left)
            res.append(root.val)
            result(root.right)
            return
        
        result(root)
        return res