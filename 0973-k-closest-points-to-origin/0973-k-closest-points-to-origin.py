class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for i in range(len(points)):
            if len(res) < k:
                heapq.heappush(res, (-(points[i][0] ** 2 + points[i][1] ** 2),[points[i][0],points       [i][1]]))
            else:
                heapq.heappushpop(res, (-(points[i][0] ** 2 + points[i][1] ** 2),[points[i][0],      points[i][1]]))
        return [res[i][1] for i in range(k)]
# Time O(n log k)
# Space O(k)