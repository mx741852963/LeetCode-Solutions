class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lenn = len(nums)
        l = 0
        r = lenn - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
# Time O(log n )
# Space O(1)