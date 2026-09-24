class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            n = nums[i]
            ans = 0
            while n:
                ans += n % 10
                n //= 10
            if ans == i:
                return ans
        return -1
# Time O(n)
# Space O(1)