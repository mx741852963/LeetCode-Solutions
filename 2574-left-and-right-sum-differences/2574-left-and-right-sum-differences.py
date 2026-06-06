class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # lenn=len(nums)
        # l_s,r_s = [0] * lenn,[0] * lenn
        # for i in range(lenn - 1):l_s[i + 1],r_s[-i - 2] = nums[i] + l_s[i],nums[-i - 1] + r_s[-i - 1]
        # return [abs(x - y) for x, y in zip(l_s, r_s)]
        left_sum,right_sum,ans  = 0,sum(nums),[] 
        for num in nums:
            right_sum -= num  
            ans.append(abs(left_sum - right_sum))
            left_sum += num 
        return ans
# Time O(n) 
# space O(1)  
