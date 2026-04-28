# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        num = []

        def recurse(curr):   
            if not curr:
                return
            num.append(curr.val)
            recurse(curr.left)
            recurse(curr.right)
        
        recurse(root)
        num = sorted(num)
        return num[k-1]

