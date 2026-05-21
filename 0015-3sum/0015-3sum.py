class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        lenn = len(nums)
        ans = []
        for i in range(lenn):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i - 1]  == nums[i]:
                continue
            left,right = i + 1, lenn-1
            while left < right:
                target = nums[i]+nums[left] + nums[right]
                if target == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                            left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif target < 0:
                    left += 1
                else: 
                    right -= 1
        return ans
# Time O(n^2)
# Space O(n)