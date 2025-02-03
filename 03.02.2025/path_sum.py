# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def pathsum(root,targetSum,st):
            if root==None:
                return False
            st+=root.val
            if root.left is None and root.right is None:
                if st==targetSum:
                    return True
                st-=root.val
                return False
            else:
                return pathsum(root.left,targetSum,st) or pathsum(root.right,targetSum,st)
        return pathsum(root,targetSum,0)
            
        
