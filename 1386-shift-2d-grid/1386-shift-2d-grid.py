class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total
        if k == 0:
            return grid
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cur_idx = i * n + j
                new_idx = (cur_idx + k) % total
                si = new_idx // n
                sj = new_idx % n
                res[si][sj] = grid[i][j]
        return res


# Time and Space  O(n*m)
