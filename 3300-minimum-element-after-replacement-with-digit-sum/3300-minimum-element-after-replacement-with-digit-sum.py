class Solution:
    def minElement(self, nums: List[int]) -> int:
        minn = float("inf")
        def collect_res(num):
            res = 0
            string = str(num)
            for i in string:
                res += int(i)
            return res
        for num in list(map(collect_res,nums)):
           minn=min(minn,num)
        return minn