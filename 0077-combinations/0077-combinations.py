class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, sol = [], []

        def backtrack(num):
            if len(sol) == k:
                ans.append(sol[:])
                return
            if num < 1: return 
            left = num
            needed = k - len(sol)
            if left > needed:
                backtrack(num - 1)
            sol.append(num)
            backtrack(num - 1)
            sol.pop()

        backtrack(n)
        return ans
# Time O(k*C(n,k))
#  Space O(k)