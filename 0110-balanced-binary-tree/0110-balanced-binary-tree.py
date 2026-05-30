# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # flag = [True]
        # def height(root):
        #     if not root:return 0
        #     left_h = height(root.left)
        #     if flag[0] is False:return 0
        #     right_h = height(root.right)
        #     if abs(left_h-right_h)>1:
        #         flag[0] = False
        #         return 0 
        #     return  1 +max(left_h,right_h)
        # height(root)
        # return flag[0]
        def check_height(node):
            if not node:return 0  
            left_height = check_height(node.left)
            if left_height == -1: return -1  
            right_height = check_height(node.right)
            if right_height == -1: return -1  
            if abs(left_height - right_height) > 1:return -1  
            return 1 + max(left_height, right_height)
        return check_height(root) != -1
    # Time O(n)
    # Space O(h)