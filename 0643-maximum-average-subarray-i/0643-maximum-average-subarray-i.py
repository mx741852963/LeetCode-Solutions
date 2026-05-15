class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        n = len(nums)
        for i in range(k):
            left += nums[i]
        max_avg = left 
        for i in range(k, n):
            left += nums[i] - nums[i - k]
            avg = left 
            max_avg = max(max_avg, avg)
        return max_avg /k


# Time : O(n)
# Space : O(1)
