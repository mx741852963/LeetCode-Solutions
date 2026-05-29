class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,lenn,maxx,max0 = 0,len(nums),0,0
        for r in range(lenn):
            if nums[r]==0:max0 += 1
            while max0 > k :
                if nums[l] == 0:max0 -= 1    
                l+=1
            maxx = max(maxx,r-l+1)
        return maxx
# Time O(n)
# Space O(1)