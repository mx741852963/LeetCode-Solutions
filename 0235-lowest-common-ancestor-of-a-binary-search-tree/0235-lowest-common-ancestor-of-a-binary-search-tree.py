# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = root
        def search(node):
            if not node : return 
            self.lca = node
            if node is p or node is q:return 
            elif node.val < p.val and node.val < q.val:search(node.right)
            elif node.val > p.val and node.val > q.val:search(node.left)
            else:return 
        search(root)
        return self.lca