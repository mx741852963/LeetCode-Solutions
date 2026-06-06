# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minn = float("inf")
        self.prev = None
        def dfs(node):
            if not node :return 
            dfs(node.left)
            if self.prev is not None:
                self.minn = min(self.minn,node.val - self.prev)
            self.prev = node.val
            dfs(node.right)
        dfs(root)
        return self.minn