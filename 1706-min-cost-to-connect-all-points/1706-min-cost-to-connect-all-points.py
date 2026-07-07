class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        min_heap = [(0, 0)]
        total_cast = 0
        while len(seen) < n:
            dist, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            total_cast += dist
            xi, yi = points[i]
            for j in range(n):
                if j in seen:
                    continue
                xj, yj = points[j]
                nei_dist = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(min_heap, (nei_dist, j))
        return total_cast
# E = n**2
# Time O(E log(E))
# Space O(E)