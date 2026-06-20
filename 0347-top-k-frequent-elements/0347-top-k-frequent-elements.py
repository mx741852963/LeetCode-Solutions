class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  Solution one 
        # return [Counter(nums).most_common(k)[i][0] for i in range(k)] 3 second
        #  Solution two
        counter = Counter(nums)
        min_heap = []
        for key, value in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (value, key))
            else:
                heapq.heappushpop(min_heap, (value, key))
        return [min_heap[i][1] for i in range(k)] # 0ms
        # Time O(n * log K)
        # space O(n)
        #  Solution three
        # n= len(nums)
        # ans = []
        # res = [0]* (n+1)
        # counter = Counter(nums)
        # for key, value in counter.items():
        #     if res[value] ==0:res[value] = [key]
        #     else:res[value].append(key)
        # for i in range(n,-1,-1):
        #     if res[i]!=0: ans.extend(res[i])
        #     if len(ans)==k:break
        # return ans #6ms
        # Time O(n)
        # space O(n)
