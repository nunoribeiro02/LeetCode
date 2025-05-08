class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        # returns height
        def dfs (curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
    
            nonlocal res
            res = max(res, left + right)
            return max(left, right) +1    

        dfs(root)
        return res      