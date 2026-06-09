class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        sub = max(nums) - min(nums)
        return sub * k 