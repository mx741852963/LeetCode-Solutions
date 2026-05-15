import sys
input = sys.stdin.read
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        lenn = len(nums)
        for i in range(k, lenn):
            cur_sum += nums[i] - nums[i - k] 
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum /k


# Time : O(n)
# Space : O(1)
