class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        ans = ''
        counter = Counter(s)
        for char, frequency in counter.items():
            heapq.heappush(res, (-frequency,char))
        while len(res) != 0:
            frequency,char = heapq.heappop(res)
            ans += char * -frequency
        return ans