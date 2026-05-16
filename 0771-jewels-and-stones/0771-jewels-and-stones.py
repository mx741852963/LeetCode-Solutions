class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sett=set(jewels)
        count =0
        for i in stones:
            if i in sett:
                count+=1
        return count
# Time  O(n + m)
# space O(n)