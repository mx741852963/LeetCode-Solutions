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

            if bal > (m - 1 - r) + (n - 1 - c) or bal < 0:
                return False
            if r == m - 1 and c == n - 1:
                return bal == 0

            res = False
            if r + 1 < m:
                if res :
                    return 
                res = res or dfs(r + 1, c, bal)
                
            if not res and c + 1 < n:
                res = res or dfs(r, c + 1, bal)

            return res

        return dfs(0, 0, 0)


# Time and Space O(m * n * (m + n))
