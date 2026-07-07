class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        p_seen = {(i, j) for i in range(m) for j in range(n) if i == 0 or j == 0}
        a_seen = {
            (i, j) for i in range(m) for j in range(n) if i == m - 1 or j == n - 1
        }

        def bfs(seen):
            que = deque(seen)
            while que:
                i, j = que.popleft()
                for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if (
                        0 <= r < m
                        and 0 <= c < n
                        and (r, c) not in seen
                        and heights[r][c] >= heights[i][j]
                    ):
                        seen.add((r, c))
                        que.append((r, c))

        bfs(p_seen)
        bfs(a_seen)

        return [list(coords) for coords in p_seen.intersection(a_seen)]
# Time and space O(m*n)