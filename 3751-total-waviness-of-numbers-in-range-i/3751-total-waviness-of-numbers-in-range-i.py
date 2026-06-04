class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1, num2 + 1):
            num = i
            res = []
            if i < 100:
                continue
            while num > 0:
                res.append(num % 10)
                num = num // 10
                j = 0
            while j < len(res) - 2:
                if (res[j] > res[j + 1] < res[j + 2]) or (res[j] < res[j + 1] > res[j + 2]):
                    count += 1
                j += 1
        return count
# Time O(n log m)
# Space O( log m)
