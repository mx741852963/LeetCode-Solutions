class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n  = len(gain)
        for i in range(n):
            if i == 0: continue
            gain[i] = gain[i] + gain[i - 1]
        maxx =  max(gain)
        return maxx if maxx >=0 else 0