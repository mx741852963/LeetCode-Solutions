class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        num_jump = 0
        end ,far = 0,0
        for i in range(n-1):
            far = max(far,i+nums[i])
            if i == end :
                num_jump +=1
                end = far 
        return num_jump
# Time O(n) Space O(1)