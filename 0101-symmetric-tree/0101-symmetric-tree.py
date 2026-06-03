# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(ro1,ro2):
            if not ro1 and not ro2: return True
            if not ro1 or not ro2: return False
            if ro1.val != ro2.val: return False
            return isMirror(ro1.left,ro2.right) and isMirror(ro1.right,ro2.left)  
        if not root: return True  
        return isMirror(root,root)
# Time O(n)
# Space O(h)