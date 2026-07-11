class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        if  not edges : return n
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans =0
        seen = set()

        for i in range(n):
            if i not in seen:
                component = []
                stk = [i]
                seen.add(i)
                while stk:
                    node = stk.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stk.append(nei)
                v_count = len(component)
                is_complete = True
                for node in component:
                    if len(graph[node]) != v_count - 1:
                        is_complete = False
                        break
                if is_complete:
                    ans += 1
        return ans
