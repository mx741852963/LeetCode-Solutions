class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        ans = []
        if len(nums) == 1 :
            ans = 1 
            return ans
        if len(nums) == 2 :
            ans = 2
            return ans
        n = len(nums)//2
        max_num = nums.index(max(nums))
        min_num = nums.index(min(nums))    
        
        min_step=len(nums[min_num:])
        max_step=len(nums[max_num:])
        ans.append(max(min_step,max_step))
    
        min_step=len(nums[:min_num+1])
        max_step=len(nums[:max_num+1])
        ans.append(max(min_step,max_step))
    
        min_step=min(len(nums[:min_num+1]),len(nums[min_num:]))
        max_step=min(len(nums[:max_num+1]),len(nums[max_num:]))
        ans.append(min_step + max_step)
        return  min(ans)