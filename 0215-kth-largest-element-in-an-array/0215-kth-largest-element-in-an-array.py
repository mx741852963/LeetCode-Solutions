class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):nums[i] = -nums[i]
        heapq.heapify(nums)
        while k > 1:
            k -= 1
            heapq.heappop(nums)
        return -nums[0]
# Time O(n + K log n)
# Space O(1)
# 
        while k > 1:
            k -= 1
            nums[nums.index(max(nums))] = 0
        return max(nums)