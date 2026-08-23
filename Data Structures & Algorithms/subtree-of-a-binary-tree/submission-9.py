# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(not root and subRoot):
            return False
        # if((not root and not subRoot) or (root and not subRoot)):
        #     return True
        if root.val == subRoot.val and self.checkTree(root, subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def checkTree(self,t,s):

        if((not t and not s) ):
            return True
        if((not t and s) or ( t and not s) or (t.val != s.val )):
            return False
        
        return (self.checkTree(t.left, s.left) and self.checkTree(t.right, s.right))