# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def get_size(node):
            if not node:
                return (0, 0)
            ls, lc = get_size(node.left)
            rs, rc = get_size(node.right)
            cur_sum = ls + rs + node.val
            cur_count = lc + rc + 1
            if node.val == cur_sum // cur_count:
                self.count += 1
            return (cur_sum, cur_count)

        get_size(root)
        return self.count
