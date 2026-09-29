class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ")" or grid[-1][-1] == "(":
            return False

        @cache
        def dfs(r, c, bal):
            bal += 1 if grid[r][c] == "(" else -1
            if bal < 0:
                return False
            if r == m - 1 and c == n - 1:
                return bal == 0
            down = dfs(r + 1, c, bal) if r + 1 < m else False
            right = dfs(r, c + 1, bal) if c + 1 < n else False

            return down or right

        return dfs(0, 0, 0)
