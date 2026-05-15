class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        for i in range(k):
            left += nums[i]
        max_avg = left 
        for i in range(k, len(nums)):
            left += nums[i] - nums[i - k]
            # avg = left 
            if left > max_avg:
                max_avg = left
        return max_avg /k


# Time : O(n)
# Space : O(1)
