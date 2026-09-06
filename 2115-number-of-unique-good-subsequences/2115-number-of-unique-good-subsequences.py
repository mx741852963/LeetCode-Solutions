class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10**9 + 7
        end_0 = 0
        end_1 = 0
        has_0 = 0
        for char in binary :
            if char =='1':
                end_1 = (end_1 + end_0 + 1)%mod
            else :
                end_0 =(end_1 + end_0 )%mod
                has_0=1
        return (end_0 + end_1 + has_0)% mod
        # Time O(n)
        # Space O(1)
        # ans, sol, n = [], [], len(binary)
        # mod = 10**9 + 7

        # def backtrack(i):
        #     if i == n:
        #         if len(sol) > 1 and sol[0] == "0":
        #             return
        #         if sol in ans:
        #             return
        #         ans.append(sol[:])
        #         return
        #     backtrack(i + 1)
        #     s = binary[i]
        #     sol.append(s)
        #     backtrack(i + 1)
        #     sol.pop()

        # backtrack(0)
        # return (len(ans) - 1) % mod
