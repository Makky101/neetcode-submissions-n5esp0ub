class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        
        count = 1

        def recurse(num,curr):
            left = right = num
            if curr.left:
                lVal = curr.left
                left = recurse(num + 1,lVal)
            if curr.right:
                rVal = curr.right
                right = recurse(num + 1,rVal)

            if left and right:
                return max(left,right)
            else:
                return num

        res = recurse(count,root)

        return res