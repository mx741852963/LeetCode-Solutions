class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_size = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = "0"
            size = 1

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                size += dfs(i + di, j + dj)
            return size

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_size = max(max_size, dfs(i, j))

        return max_size


# Time O(n*m)
# SpaceO(n*m)
