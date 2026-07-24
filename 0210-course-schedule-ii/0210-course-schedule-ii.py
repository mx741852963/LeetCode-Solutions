class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        # unvisted = 0
        # visiting = 1
        # visited = 2
        states = [0] * numCourses
        ans = []
        def dfs(node):
            state = states[node]
            if state == 2:
                return True
            elif state == 1:
                return False
            states[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            states[node] = 2
            ans.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
# Time O(V+E)
# Space O(V+E)