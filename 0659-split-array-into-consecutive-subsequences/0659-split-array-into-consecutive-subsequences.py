class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        chains = defaultdict(list)
        for num in nums:
            if chains[num - 1]:
                length = heapq.heappop(chains[num - 1])
                heapq.heappush(chains[num], length + 1)
            else:
                heapq.heappush(chains[num], 1)
        for last_num in chains:
            for length in chains[last_num]:
                if length < 3:
                   return False 
        return True