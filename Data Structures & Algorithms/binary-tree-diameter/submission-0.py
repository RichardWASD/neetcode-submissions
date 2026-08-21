# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1st node counts as 0 then the length
        '''
        setup dfs algo 

        special condition: Setup a new count for each node -> save max to result and continue this downwards
        '''
        res = 0;
        
        def dfs(curr):
            if not curr: 
                return 0
            nonlocal res
            left = dfs(curr.left)
            right = dfs(curr.right)
            res = max(res, left+right)
            return 1 + max(left,right)
        dfs(root) 
        return res


