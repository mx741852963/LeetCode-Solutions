class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # closest_x = 0
        # if xCenter < x1:
        #     closest_x = x1
        # elif xCenter > x2:
        #     closest_x = x2
        # else:
        #     closest_x = xCenter
        # closest_y = 0
        # if yCenter < y1:
        #     closest_y = y1
        # elif yCenter > y2:
        #     closest_y = y2
        # else:
        #     closest_y = yCenter
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        return (dx**2 + dy**2) <= (radius**2)
        # Time and Spcae O(1)
