class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hash_map = []
        counter = defaultdict(int)
        for sender, message in zip(senders, messages):
            counter[sender]+=len(message.split())
        for key , value in counter.items():
            if len(hash_map) < 1:
                heapq.heappush(hash_map, (value, key))
            else:
                heapq.heappushpop(hash_map, (value, key))
        return hash_map[0][1]