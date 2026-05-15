class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        prev= 0
        cur = 1 
        for i in range(2,n+1):
            prev,cur = cur,cur+prev
        return cur
# Time O(n)
# Space O(1)


# class Solution:
#     def fib(self, n: int) -> int:
#         if n==0:
#             return 0
#         if n==1:
#             return 1
#         dp = [0]*(n+1)
#         dp[0]=0
#         dp[1]=1
#         for i in range(2,n+1):
#             dp[i] = dp[i-2]+dp[i-1]
#         return dp[-1]
# Time O(n)
# Space O(n)



# class Solution:
#     def fib(self, n: int) -> int:
#         cache = {0:0,1:1}
#         def f(num):
#             if num in cache:
#                 return cache[num]
#             else:
#                 cache[num] = f(num-1)+f(num-2)
#                 return cache[num]
#         return f(n)
# Time O(n)
# Space O(n)