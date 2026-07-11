class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)
        q = deque([source])
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        return False
        # Time and Space O(V+E)


        # sol 2
        # stk = [source]
        # while stk:
        #     node = stk.pop()
        #     if node == destination:
        #         return True
        #     for nei in graph[node]:
        #         if nei not in seen:
        #             seen.add(nei)
        #             stk.append(nei)
        # return False


        # sol 1
        # def dfs (i):
        #     if i == destination:
        #         return True
        #     for nei in graph[i]:
        #         if nei not in seen:
        #             seen.add(nei)
        #             if dfs(nei):
        #                 return True
        #     return False

        # return dfs(source)
