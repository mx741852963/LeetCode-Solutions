class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, sol, n = [], [], len(nums)
        visited = set()

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    sol.append(num)
                    backtrack()
                    sol.pop()
                    visited.remove(num)

        backtrack()
        return ans


# Time O(n*n!)
# Space O(n)
