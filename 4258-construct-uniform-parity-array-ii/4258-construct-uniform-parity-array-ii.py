class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
      n=len(nums1)
      if min(nums1)&1 : return True 
      else :
        return False if max([x & 1 for x in nums1 ]) else True  
