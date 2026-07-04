class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []
        n = len(nums)
        # count = Counter(nums)
        visited = set()
        def backtrack():
            if len(sol) == n and sol[:] not in ans:
                ans.append(sol[:])
                return
            for i in range(n):
                if i  not in visited:
                    visited.add(i)
                    # count[num]-=1
                    sol.append(nums[i])
                    backtrack()
                    sol.pop()
                    visited.remove(i)
                    # count[num]+=1
        backtrack()

        return ans
