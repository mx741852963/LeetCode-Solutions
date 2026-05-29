class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        lenn = len (nums)
        minn = float('inf')
        count = 0
        if target in nums:
            return 1
        for r in range(lenn):
            count += nums[r]
            while count >= target:
                minn = min(minn,r-l+1)
                count -=nums[l]
                l +=1
        return minn if minn !=float('inf') else 0
# Time O(n)
# Space O(1)