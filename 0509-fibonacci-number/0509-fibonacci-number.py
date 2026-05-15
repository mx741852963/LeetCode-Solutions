class Solution:
    def fib(self, n: int) -> int:
        cache = {0:0,1:1}
        def f(num):
            if num in cache:
                return cache[num]
            else:
                cache[num] = f(num-1)+f(num-2)
                return cache[num]
        return f(n)
# Time O(n)
# Space O(n)