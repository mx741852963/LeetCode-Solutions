class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            y = target - num
            if y in h:
                return [h[y], i]
            h[num] = i
        # for  i in range (len(nums)):
        #     h[nums[i]] = i
        # for i in range (len(nums)):
        #     y = target - nums[i]
        #     if y in h and h[y] != i:
        #         return [i,h[y]]
# Time = O(n) # Space = O(n)


