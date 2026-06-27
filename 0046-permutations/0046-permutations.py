class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, sol, n = [], [], len(nums)

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans
# Time O(n!)
# Space O(n)