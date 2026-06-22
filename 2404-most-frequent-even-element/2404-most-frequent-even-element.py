class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter(nums)
        heap = []
        for key,value in counter.items():
            if (key&1)==0:
                if len(heap) < 1:
                    heapq.heappush(heap, (value, -key))
                else:heapq.heappushpop(heap, (value, -key))
        if heap : return -heap[0][1] 
        else : return -1
         