class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # chains = defaultdict(list)
        # for num in nums:
        #     if chains[num - 1]:
        #         length = heapq.heappop(chains[num - 1])
        #         heapq.heappush(chains[num], length + 1)
        #     else:
        #         heapq.heappush(chains[num], 1)
        # for last_num in chains:
        #     for length in chains[last_num]:
        #         if length < 3:
        #            return False 
        # return True
# Time O(n log k)
# Space O(n)
        counter = collections.Counter(nums)
        hash_map = collections.defaultdict(int)
        for num in nums:
            if counter[num]==0:continue
            counter[num]-=1
            if hash_map[num-1]>0:
                hash_map[num-1]-=1
                hash_map[num]+=1
            elif counter[num+1] >0 and counter[num+2]>0:
                counter[num+1] -=1
                counter[num+2] -=1
                hash_map[num+2] +=1
            else:return False
        return True
