class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        if min(nums) > x:
            return -1
        target = sum(nums) - x
        max_len = -1
        cur_sum = 0
        l = 0
        n = len(nums)
        for r in range(n):
            cur_sum += nums[r]
            while cur_sum > target and l <= r:
                cur_sum -= nums[l]
                l += 1
            if cur_sum == target:
                max_len = max(max_len, r - l + 1)
        return n - max_len if max_len != -1 else -1
