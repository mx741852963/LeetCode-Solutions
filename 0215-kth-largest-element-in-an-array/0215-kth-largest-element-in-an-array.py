class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # for i in range(len(nums)):nums[i] = -nums[i]
        # heapq.heapify(nums)
        # while k > 1:
        #     k -= 1
        #     heapq.heappop(nums)
        # return -nums[0]
# Time O(n + K log n)
# Space O(1)
# 
# Time Limit Exceeded
        # while k > 1:
        #     k -= 1
        #     nums[nums.index(max(nums))] =  -float("inf")
        # return max(nums)
# 
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]
# Time O(n log k)
# Space O(K)