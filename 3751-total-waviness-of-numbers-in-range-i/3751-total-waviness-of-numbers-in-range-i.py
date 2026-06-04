class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wave  = 0
        if num1 < 100:
            num1 = 101
        for i in range(num1, num2 + 1):
            num = str(i)
            j = 0
            while j < len(num) - 2:
                l = num[j]
                m = num[j + 1]
                r = num[j + 2]
                if m > max(r, l) or m < min(l, r):
                    wave += 1
                j += 1
        return wave
#         count = 0
#         if num1 < 100:
#             num1 =101
#         for i in range(num1, num2 + 1):
#             num = i
#             res = []
#             while num > 0:
#                 res.append(num % 10)
#                 num = num // 10
#                 j = 0
#             while j < len(res) - 2:
#                 l = res[j]
#                 m = res[j + 1]
#                 r = res[j + 2]
#                 if m > max(r,l) or m < min(l,r):
#                     count += 1
#                 j += 1
#         return count
# # Time O(n log m)
# # Space O( log m)
