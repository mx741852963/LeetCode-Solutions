class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_I = sorted(intervals, key=lambda t: t[0])
        ans= []
        for interval in sorted_I:
            if not ans or ans[-1][1]<interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
# Time O(n log n )
# Space O(n)