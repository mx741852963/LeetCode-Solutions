class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = stones.__len__()
        for i in range(n):stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1 :
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)
            if largest != next_largest:heapq.heappush(stones, largest-next_largest)
        return -stones[0] if stones else 0
# Time O(n log n)
# Space O(1)