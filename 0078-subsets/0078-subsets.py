class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lenn = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == lenn:
                res.append(sol[:])
                return
            backtrack(i + 1)
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return res
# Time O(n*2**n)
# Space O(n*2**n) 