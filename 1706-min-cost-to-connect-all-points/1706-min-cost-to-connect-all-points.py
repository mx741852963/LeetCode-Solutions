class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        min_heap = []
        total_cast = 0
        start_node = 0 
        seen.add(start_node) 
        xi, yi = points[start_node]
        for j in range(n):
            if j != start_node:  
                xj, yj = points[j]
                nei_dist = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(min_heap, (nei_dist, j))
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
# E =(n * (n-1))/2 
# E = n**2
# Time O(E log(E))
# Space O(E)