class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []
        n = len(nums)
        visited = set()
        def backtrack():
            if len(sol) == n and sol[:] not in ans:
                ans.append(sol[:])
                return
            for i in range(n):
                if i  not in visited:
                    visited.add(i)
                    sol.append(nums[i])
                    backtrack()
                    sol.pop()
                    visited.remove(i)
        backtrack()
        return ans
