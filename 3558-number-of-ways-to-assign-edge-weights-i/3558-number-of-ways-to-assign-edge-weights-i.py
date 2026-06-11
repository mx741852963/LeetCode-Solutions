class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        seen = set()
        seen.add(1)
        q = deque([(1, 0)])
        max_depth = 0
        while q:
            node, depth = q.popleft()
            if depth > max_depth:
                max_depth = depth
            for nei_node in adjacency_list[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append((nei_node, depth + 1))
            
        return pow(2, max_depth - 1, 10**9 + 7)
# Time O(n)
# Space O(n)