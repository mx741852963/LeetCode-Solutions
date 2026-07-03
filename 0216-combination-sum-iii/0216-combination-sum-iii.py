class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
                ans, sol = [], []
                def backtrack(num, cur_sum):
                    if num <0 : return
                    if cur_sum == n and len(sol)==k:
                        ans.append(sol[:]) 
                        return
                    left = num
                    needed = k - len(sol)
                    if left> needed:
                        backtrack(num-1,cur_sum)
                    sol.append(num)
                    backtrack(num-1,cur_sum+ num)
                    sol.pop()
                backtrack(9,0)
                return ans
