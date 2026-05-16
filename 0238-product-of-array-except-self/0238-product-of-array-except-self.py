class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            r = [1]
            l = [1]
            ans=[]
            i = 0
            j = 0
            while i < len(nums) - 1:
                l.append(l[j] * nums[i])
                i += 1
                j = i
            nums.reverse()
            i = 0
            j = 0
            while i < len(nums) - 1:
                r.append(r[j] * nums[i])
                i += 1
                j = i
            r.reverse()
            x=0
            while x < len(nums):
                ans.append(r[x]*l[x])
                x += 1
            return ans