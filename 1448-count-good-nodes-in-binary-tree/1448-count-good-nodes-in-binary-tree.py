from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append((root,root.val))
        count = 0
        while q: 
            node,maxx = q.popleft()
            if maxx <= node.val: count +=1
            maxx = max(maxx,node.val)
            if node.left : q.append((node.left,maxx))
            if node.right : q.append((node.right,maxx))
        return count
        