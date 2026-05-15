class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        n = len(nums)
        for i in range(k):
            left += nums[i]
        max_avg = left / k
        for i in range(k, n):
            left += nums[i]
            left -= nums[i - k]
            avg = left / k
            max_avg = max(max_avg, avg)
        return max_avg
# Time : O(n)
# Space : O(1)