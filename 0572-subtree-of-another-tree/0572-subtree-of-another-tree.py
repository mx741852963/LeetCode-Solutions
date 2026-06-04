from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree( p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q: return True
            if not p or not q: return False
            if p.val!=q.val:return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        if not root:return False
        q = deque()
        q.append(root)
        while q: # BFS Time O(m*n) Space O(W_root + H_sub)
            node = q.popleft()
            if isSameTree(node,subRoot):return True
            if node.left : q.append(node.left)
            if node.right : q .append(node.right)
        return False
        # def has_subtree(root):# DFS Time O(m*n) Space O(H_root + H_sub)
        #     if not root:return False
        #     if isSameTree(root,subRoot):return True
        #     return has_subtree(root.left) or has_subtree(root.right)
        # return has_subtree(root)