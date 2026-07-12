class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {val: rank + 1 for rank, val in enumerate(sorted(set(arr)))}
        return [ranks[x] for x in arr]
        # arr2,arr3 = list(set(arr)),{}
        # n,m = len(arr2),len(arr)
        # arr2.sort()
        # for i in range(n):
        #     arr3[arr2[i]] = i + 1
        # return [arr3[i] for i in arr]
# Time O(n log n)
# Space O(n)