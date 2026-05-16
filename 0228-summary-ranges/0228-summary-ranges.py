class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        num = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                i += 1
            if start == nums[i]:
                num.append(str(start))
            else:
                num.append(f"{start}->{nums[i]}")
            i = i + 1
        return num
# Time : O(n)
# Space : O(n)   