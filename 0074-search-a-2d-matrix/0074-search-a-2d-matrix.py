class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        target_row = -1
        while top <= bot:
            mid_row = (top + bot) // 2
            if target < matrix[mid_row][0]:
                bot = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                target_row = mid_row
                break
        if target_row == -1:
            return False
        row = matrix[target_row]
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
#         t = m * n
#         l = 0
#         r = t - 1
#         while l <= r:
#             mid = (l + r) // 2
#             i = mid // n
#             j = mid % n
#             mid_nums = matrix[i][j]
#             if mid_nums == target:
#                 return True
#             elif mid_nums < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return False
# # Time O(log(m * n))
# # Space O(1)