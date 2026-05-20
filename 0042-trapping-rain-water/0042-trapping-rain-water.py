class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall = right_wall = 0
        lenn = len(height)
        max_left = [0]*lenn
        max_right = [0]*lenn
        summ =  0
        for i in range(lenn):
            j = -i -1
            max_left[i],max_right[j]=left_wall,right_wall
            left_wall,right_wall = max(left_wall,height[i]),max(right_wall,height[j])
        for i in range(lenn):
            pot = min(max_left[i],max_right[i])
            summ += max(0,pot-height[i])
        return summ 
        # Time O(n)
        # Space O(n)
        # maxx = max(height)
        # count = 0
        # for m in range(0, maxx):
        #     if len(height) <= 0 or maxx == 0:
        #         break
        #     left_side = 0
        #     right_side = len(height) - 1
        #     while True:
        #         if height[left_side] > 0 and height[right_side] > 0:
        #             break
        #         if height[left_side] == 0:
        #             left_side += 1
        #         if height[right_side] == 0:
        #             right_side -= 1

        #     for c in range(left_side, right_side):
        #         if height[c] == 0:
        #             count += 1
        #     height = [i - 1 if i > 0 else 0 for i in height]
        # return count