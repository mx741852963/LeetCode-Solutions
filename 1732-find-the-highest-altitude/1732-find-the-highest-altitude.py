class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # n  = len(gain)
        # maxx = 0
        # for i in range(1,n):
        #     gain[i] = gain[i] + gain[i - 1] 
        # maxx =  max(gain)
        # return maxx if maxx >=0 else 0
# Time O(n)
# Space O(1)
        maxx = 0 
        cur_altitude = 0
        for g in gain :
            cur_altitude += g
            if cur_altitude > maxx : maxx = cur_altitude
        return maxx
# Time O(n)
# Space O(n)