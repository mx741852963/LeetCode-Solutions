from collections import Counter
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        counts = Counter(nums)
        unique = sorted(counts.keys())
        result = []
        if len(nums) < 3:
            return []
        if counts[0] >= 3:
            result.append([0, 0, 0])
        del counts[0] 
        for i, num1 in enumerate(unique):
            for num2 in unique[i:]:
                if num1 == num2 and counts[num1] < 2:
                    continue
                num3 = -num1 - num2
                if num3 < num2: 
                    continue
                if num3 in counts:
                    if num2 == num3 and counts[num2] < 2:
                        continue
                    result.append([num1, num2, num3])

        return result
#         nums.sort()
#         lenn = len(nums)
#         ans = []
#         for i in range(lenn):
#             if nums[i] > 0:
#                 break
#             elif i > 0 and nums[i - 1]  == nums[i]:
#                 continue
#             left,right = i + 1, lenn-1
#             while left < right:
#                 target = nums[i]+nums[left] + nums[right]
#                 if target == 0:
#                     ans.append([nums[i],nums[left],nums[right]])
#                     left += 1
#                     right -= 1
#                     while left < right and nums[left] == nums[left-1]:
#                             left += 1
#                     while left < right and nums[right] == nums[right+1]:
#                         right -= 1
#                 elif target < 0:
#                     left += 1
#                 else: 
#                     right -= 1
#         return ans
# # Time O(n^2)
# # Space O(n)