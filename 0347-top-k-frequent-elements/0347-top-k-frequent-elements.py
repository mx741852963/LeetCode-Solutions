class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [Counter(nums).most_common(k)[i][0] for i in range(k)] 3 second
        counter = Counter(nums)
        min_heap = []
        for key, value in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (value, key))
            else:
                heapq.heappushpop(min_heap, (value, key))
        return [min_heap[i][1] for i in range(k)]