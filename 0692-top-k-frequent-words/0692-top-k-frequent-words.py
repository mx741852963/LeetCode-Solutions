class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        max_heap,res = [],[]
        for key, value in counter.items(): heapq.heappush(max_heap, (-value, key))
        while k :
            k-=1
            _ ,key = heapq.heappop(max_heap)
            res.append(key)
        return res

        # Time O(n log k)
        # Space O(k)