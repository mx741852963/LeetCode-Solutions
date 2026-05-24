class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lenn = len(nums)
        r = lenn - 1
        l = 0
        while l <=r :
            mid = (r+l)//2
            if nums[mid] < target :
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid 
        return mid + 1  if target > nums[mid] else mid 
