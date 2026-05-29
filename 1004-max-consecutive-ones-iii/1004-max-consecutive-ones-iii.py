class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r,maxx = 0,0,0
        lenn = len(nums)
        while l  < lenn and r < lenn:
            if nums[r] == 1 :r += 1
            elif nums[r] == 0 and k !=0:
                k -= 1
                r += 1
            else :
                while k == 0:
                    if nums[l] == 0:
                        k += 1
                    l +=1
            maxx = max(maxx, r - l)
        return maxx
