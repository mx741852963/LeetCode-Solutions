class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenn = len(nums)
        r = lenn - 1
        l = 0 
        if nums[l] <= nums[r]:
            return nums[l]
        while l < r :
            mid = (r+l)//2
            if nums[mid] > nums[r]:
                l  = mid + 1 
            else :
                r = mid
        return nums[l]
        # Time O(log n )
        # Space O(1)
        # target = float('inf')
        # if nums[l] <= nums[r]:
        #     return nums[l]
        # while l <= r :
        #     mid = (l+r)//2
        #     if nums[r] < nums[mid]:
        #         target = min(nums[mid],target)
        #         l = mid + 1
        #     else:
        #         target = min(nums[mid],target)
        #         r = mid - 1
        # return target 