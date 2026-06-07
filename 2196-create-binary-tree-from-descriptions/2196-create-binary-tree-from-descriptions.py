# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes,children = {},set()
        for description in descriptions :
            parent,child,isleft = description[0],description[1],bool(description[2])
            nodes.setdefault(parent,TreeNode(parent))
            nodes.setdefault(child,TreeNode(child))
            if isleft:nodes[parent].left = nodes[child]
            else:nodes[parent].right= nodes[child]
            children.add(child)
        for node in nodes.values():
            if node.val not in children:return node
# Time O(n)
# Space O(n)