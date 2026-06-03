# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx = [0]
        def check_diameter(node):
            if not node : return 0
            left = check_diameter(node.left)
            right = check_diameter(node.right)
            maxx[0] = max(maxx[0],left+right)
            return 1+max(left,right)
        check_diameter(root)
        return maxx[0]