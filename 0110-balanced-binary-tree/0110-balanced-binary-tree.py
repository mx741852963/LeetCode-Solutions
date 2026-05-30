# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = [True]
        def height(root):
            if not root:return 0
            left_h = height(root.left)
            if flag[0] is False:return 0
            right_h = height(root.right)
            if abs(left_h-right_h)>1:
                flag[0] = False
                return 0 
            return  1 +max(left_h,right_h)
        height(root)
        return flag[0]
    # Time O(n)
    # Space O(h)