class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1 :
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)
            if largest != next_largest:heapq.heappush(stones, largest-next_largest)

        if len(stones)==1:return -stones[-1]
        else:return 0