class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        r = restrictions
        r.append([1, 0])
        r.sort()
        if r[-1][0] != n:
            r.append([n, n - 1])
        lenn = len(r)
        for i in range(1, lenn):
            r[i][1] = min(r[i][1], r[i - 1][1] + (r[i][0] - r[i - 1][0]))
        for i in range(lenn - 2, -1, -1):
            r[i][1] = min(r[i][1], r[i + 1][1] + (r[i + 1][0] - r[i][0]))
        res = 0
        for i in range(lenn - 1):
            tem = ((r[i + 1][0] - r[i][0]) + r[i][1] + r[i + 1][1]) // 2
            res = max(res, tem)
        return res
# Time O(n)
# Space O(n)