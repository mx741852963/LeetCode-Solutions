# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def get_size(node):
            if not node:
                return (0, 0, 0)
            ls, lc, lv = get_size(node.left)
            rs, rc, rv = get_size(node.right)
            cur_sum = ls + rs + node.val
            cur_count = lc + rc + 1
            is_valid = 1 if (cur_sum // cur_count) == node.val else 0
            return (cur_sum, cur_count, lv + rv + is_valid)

        return get_size(root)[2]


# Time O(n)
# Space O(h)
