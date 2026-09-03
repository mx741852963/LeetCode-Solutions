class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
      return True if min(nums1)&1  else not any(x & 1 for x in nums1)
# Time O(n) Space O(1)