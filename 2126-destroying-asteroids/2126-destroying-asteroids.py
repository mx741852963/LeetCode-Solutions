class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        summ = 0
        if asteroids[0]<=mass:
            summ = mass + asteroids[0]
            for  i in range(1,len(asteroids)):
                if asteroids[i]>summ:
                    return False
                summ += asteroids[i]
            return True 
        return False