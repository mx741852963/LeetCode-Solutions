class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(self.get_height(heights), max_area)
        return max_area

    def get_height(self,heights):
        stk = []
        n = len(heights)
        max_area = 0
        for i, height in enumerate(heights):
            start = i
            while stk and height < stk[-1][0]:
                h, j = stk.pop()
                w = i - j
                a = h * w
                max_area = max(max_area, a)
                start = j
            stk.append((height, start))
        while stk:
            h, j = stk.pop()
            w = n - j
            max_area = max(max_area, w * h)
        print(heights)
        return max_area


# Time O(rows * cols )
# Space O(cols)
