class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        ans, sol = [], []
        n = len(candidates)
        def backtrack(start, cur_sum):
            if cur_sum == target:
                ans.append(sol[:]) 
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if cur_sum + candidates[i] <= target:
                    sol.append(candidates[i])
                    backtrack(i + 1, cur_sum + candidates[i])
                    sol.pop()
                else:break           
        backtrack(0, 0)
        return ans
# Time O(2**n)
# Space O(n)