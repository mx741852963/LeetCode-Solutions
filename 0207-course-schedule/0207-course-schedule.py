class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        # unvisted = 0
        # visiting = 1
        # visited = 2
        states = [0] * numCourses

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
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
