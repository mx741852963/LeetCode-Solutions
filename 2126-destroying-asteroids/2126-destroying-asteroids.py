class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        summ = mass
        lenn=len(asteroids)
        for i in range(lenn):
            if asteroids[i] > summ:
                return False
            summ += asteroids[i]
        return True
        # Time O(n log n)
        # space O(n)
        # if asteroids[0]<=mass:
        #     summ = mass + asteroids[0]
        #     for  i in range(1,len(asteroids)):
        #         if asteroids[i]>summ:
        #             return False
        #         summ += asteroids[i]
        #     return True 
        # return False