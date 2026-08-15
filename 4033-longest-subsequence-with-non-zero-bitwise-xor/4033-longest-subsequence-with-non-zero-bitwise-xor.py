from functools import reduce
from operator import xor


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        res = reduce(xor, nums)
        if res != 0:
            return len(nums)
        return len(nums) - 1 if any(x != 0 for x in nums) else 0
# Time O(n)
# Spcae O(1)