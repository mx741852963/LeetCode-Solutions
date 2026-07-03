class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
                ans, sol = [], []
                def backtrack(num, cur_sum):
                    if len(sol)==k:
                        if cur_sum == n :
                            ans.append(sol[:]) 
                        return
                    if cur_sum > n :return
                    left = num
                    needed = k - len(sol)
                    if left> needed:
                        backtrack(num-1,cur_sum)
                    if num > 0:
                        sol.append(num)
                        backtrack(num-1,cur_sum+ num)
                        sol.pop()
                backtrack(9,0)
                return ans
