class WordItem:
    def __init__(self, freq: int, word: str):
        self.freq = freq
        self.word = word

    def __lt__(self, other: "WordItem") -> bool:
        if self.freq != other.freq: return self.freq < other.freq
        return self.word > other.word

    def __repr__(self) -> str:
        return self.word
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for key, value in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, WordItem(value, key))
            else:
                heapq.heappushpop(heap, WordItem(value, key))
        res = []
        while heap:
            item = heapq.heappop(heap)
            res.append(item.word) 
        return res[::-1]


        # Time O(n log k)
        # Space O(n)

        # counter = Counter(words)
        # max_heap,res = [],[]
        # for key, value in counter.items(): heapq.heappush(max_heap, (-value, key))
        # while k :
        #     k-=1
        #     _ ,key = heapq.heappop(max_heap)
        #     res.extend([key])
        # return res
        # Time O(n + u log u)