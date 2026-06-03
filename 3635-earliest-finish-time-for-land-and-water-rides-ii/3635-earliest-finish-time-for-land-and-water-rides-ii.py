import heapq
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_end_land = min(s + d for s, d in zip(landStartTime, landDuration))
        ans_land_water = min(max(min_end_land, s) + d for s, d in zip(waterStartTime, waterDuration))
        min_end_water = min(s + d for s, d in zip(waterStartTime, waterDuration))
        ans_water_land = min(max(min_end_water, s) + d for s, d in zip(landStartTime, landDuration))
        return min(ans_land_water, ans_water_land)
    # Time  O(n+m)
    # Space O(1)