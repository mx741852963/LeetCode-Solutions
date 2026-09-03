class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
      if min(nums1)&1 : return True 
      else :return False if 1 in [x & 1 for x in nums1 ] else True  
