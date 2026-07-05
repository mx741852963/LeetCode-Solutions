class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lenn = len(nums)
        res, sol = [], []
        visited = set()
        nums.sort()
        def backtrack(i):
            if i == lenn:
                res.append(sol[:])
                return 
            backtrack(i + 1)
            if i in visited:
                return
            if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited:
                return
            visited.add(i)
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
            visited.remove(i)

        backtrack(0)
        return res
# Time O(2^n)
# Space O(n) 