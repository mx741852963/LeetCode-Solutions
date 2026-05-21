class Solution:
    def maxArea(self, height: List[int]) -> int:
        lenn = len(height)
        left = 0
        right = lenn - 1
        max_area = 0
        if not height:
            return 0
        while left < right:
            l = height[left]
            r = height[right]
            size = min(r,l) * (lenn - 1)
            max_area = max(max_area,size)
            if l < r :
                left += 1
                lenn -=1
            if l > r :
                right -= 1
                lenn -=1
            if l == r:
                left += 1
                # right -= 1
                lenn -= 1
        return max_area