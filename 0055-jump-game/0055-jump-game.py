class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # @cache
        # def can_reach(i):
        #     if i ==n-1:
        #         return True
        #     for j in range(1,nums[i]+1):
        #         if can_reach(i+j):
        #             return True
        #     return False
        # return can_reach(0)


        # Greedy
        # Time O(n)
        # Space O(1)
        n = len(nums)
        target = n-1
        for i in range(n-1,-1,-1):
            jump = nums[i]
            if i +jump >= target:
                target = i
        return target == 0

            
        