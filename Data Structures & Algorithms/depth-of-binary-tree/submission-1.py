# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       

        if not root:
            return 0
        # def dfs(node,depth):
        #     if(not node):
        #         return 0
        #     if node.left and node.right:
        #         return max(dfs(root.left), dfs(root.right))
        #     if node.left:
        #         return dfs(node.left, depth + 1)
        #     if node.right:
        #        return  dfs(node.right, depth + 1)
            

        res = 0
        depth = 1
        s = [[root,depth]]   
        while s:
            node, depth = s.pop()

            if node.left:
                s.append([node.left, depth + 1 ])
            if node.right:
                s.append([node.right, depth + 1])
            res = max(res,depth)
        
        return res

