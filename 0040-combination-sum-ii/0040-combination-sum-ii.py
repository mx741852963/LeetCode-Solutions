class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, sol = [], []
        n = len(candidates)
        visited = [False for _ in range(n)]
        def backtrack(i, cur_sum):
            if cur_sum == target:
                ans.append(sol[:])
                return
            if cur_sum > target or i == n:
                return
            backtrack(i + 1, cur_sum)
            if i > 0 and candidates[i] == candidates[i-1] and not visited[i-1]:
                return   
            sol.append(candidates[i])
            visited[i] = True
            backtrack(i + 1, cur_sum + candidates[i])
            sol.pop()
            visited[i] = False
        backtrack(0, 0)
        return ans