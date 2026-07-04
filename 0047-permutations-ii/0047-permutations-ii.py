class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []
        n = len(nums)
        nums.sort()

        visited = set()
        def backtrack():
            if len(sol) == n and sol[:] not in ans:
                ans.append(sol[:])
                return
            for i in range(n):
                if i   in visited:
                    continue
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited:
                    continue
                visited.add(i)
                sol.append(nums[i])
                backtrack()
                sol.pop()
                visited.remove(i)

        backtrack()

        return ans
