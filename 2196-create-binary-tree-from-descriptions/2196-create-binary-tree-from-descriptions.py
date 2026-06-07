# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes,children = defaultdict(lambda: TreeNode(None)),set()
        for parent, child, isleft in descriptions :
            if nodes[parent].val is None: nodes[parent].val = parent
            if nodes[child].val is None: nodes[child].val = child
            if isleft:nodes[parent].left = nodes[child]
            else:nodes[parent].right= nodes[child]
            children.add(child)
        for node in nodes:
            if node not in children:return nodes[node]
# Time O(n)
# Space O(n)