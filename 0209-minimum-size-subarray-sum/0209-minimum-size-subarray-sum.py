class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        lenn = len (nums)
        minn = float('inf')
        summ = 0
        for r in range(lenn):
            summ += nums[r]
            while summ >= target:
                minn = min(minn,r-l+1)
                summ -=nums[l]
                l +=1
        return minn if minn !=float('inf') else 0
# Time O(n)
# Space O(1)