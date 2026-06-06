# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return 0
        q=deque([root])
        res = []
        while q:
            avg = 0
            lenn = len(q)
            for i in range(lenn):
                node = q.popleft()
                avg+=node.val
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            res.append(avg/lenn)
        return res
# Time O(n)
# Space O(n)