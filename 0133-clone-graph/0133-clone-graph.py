"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :return None
        start = node
        hash = {}
        stk = [start]
        visited = set()
        visited.add(start)
        while stk:
            node  = stk.pop()
            hash[node] =Node(val=node.val)
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)
        for old , new in hash.items():
            for nei in old.neighbors:
                new_nei = hash[nei]
                new.neighbors.append(new_nei)
        return hash[start]
# Time O(V+E)
# space O(V)
