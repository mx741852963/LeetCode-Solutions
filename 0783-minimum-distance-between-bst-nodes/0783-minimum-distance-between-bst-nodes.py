# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node,prev,minn):
            if not node or minn==1 :return prev,minn
            prev,minn = dfs(node.left,prev,minn)
            if minn==1 : return prev,minn
            if prev is not None:minn = min(minn,node.val - prev)
            prev = node.val
            return dfs(node.right,prev,minn)
        _,minn = dfs(root,None,inf)
        return minn 
# Time O(n)
# Space O(n)